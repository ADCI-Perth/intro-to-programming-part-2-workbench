"""Convert the Part 2 course repo into Carpentries Workbench episodes: one episode per week.
Each week page holds the week overview, its sections, the Concepts Bridge and the practice task
as level-2 headings, so the Workbench menu shows Week N with 1.1, 1.2 ... underneath.
Usage: python scripts/convert_from_course.py SOURCE_REPO LESSON_REPO"""
import os, posixpath, re, shutil, sys, zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wb_meta import WEEKS, TIME, SECTIONS, OPTIONAL, BRIDGES, PRACTICE, PRACTICE_Q

SRC, DST = sys.argv[1], sys.argv[2]
W = os.path.join(SRC, 'weeks')
EP = os.path.join(DST, 'episodes')
ZIP_ROOT = 'IntroToProgrammingPart2'

# ---------------------------------------------------------------- names
def week_file(w): return f'week-{w}.md'
def sec_anchor(s): return 'section-' + s.replace('.', '-')
def opt_file(s, slug): return f"{s.replace('.', '-')}-{slug}.md"

TARGET = {}   # source path (relative to SRC, posix) -> (folder, filename, anchor)
for s, m in SECTIONS.items():
    TARGET['weeks/' + m['src']] = ('episodes', week_file(int(s[0])), sec_anchor(s))
for s, m in OPTIONAL.items():
    TARGET['weeks/' + m['src']] = ('learners', opt_file(s, m['slug']), '')
for w in WEEKS:
    TARGET[f'weeks/week-{w}/README.md'] = ('episodes', week_file(w), f'week-{w}-overview')
    TARGET[f'weeks/week-{w}/bridge.md'] = ('episodes', week_file(w), f'week-{w}-bridge')
    TARGET[f'weeks/week-{w}/practice/README.md'] = ('episodes', week_file(w), f'week-{w}-practice')
for w, m in PRACTICE.items():
    for f in m['files']:
        TARGET[f'weeks/week-{w}/practice/{f}'] = ('episodes', f'files/week-{w}/{f}', '')

# ---------------------------------------------------------------- text helpers
FENCE = {'py': 'python', 'python': 'python', 'pycon': 'python', 'text': 'output',
         'sh': 'bash', 'shell': 'bash', 'bash': 'bash'}


def fences(t):
    return re.sub(r'^(\s*)```(\w+)\s*$', lambda m: m.group(1) + '```' + FENCE.get(m.group(2), m.group(2)), t, flags=re.M)


def links(t, src_rel, here, page):
    """Rewrite relative links in text from source file src_rel, for the page `page` in folder `here`."""
    base = posixpath.dirname(src_rel)

    def fix(m):
        label, url = m.group(1), m.group(2)
        if re.match(r'^(https?:|mailto:|#)', url):
            return m.group(0)
        path, _, frag = url.partition('#')
        target = posixpath.normpath(posixpath.join(base, path))
        if target.startswith('assets/data/'):
            return f'[{label}](data/{target[len("assets/data/"):]})'
        if target.startswith('assets/files/'):
            return f'[{label}](files/{target[len("assets/files/"):]})'
        if target in ('assets/data', 'assets/data/', 'assets/files', 'assets/files/'):
            return f'[{label}](data/course-data.zip)'   # web hosts do not list folders
        code = re.match(r'weeks/week-\d/lessons/(\d\.\d)_code(/.*)?$', target)
        if code:
            return f'[{label}](files/code/{code.group(1)}{code.group(2) or "/"})'
        bridge = re.match(r'weeks/week-(\d)/bridge_code(/.*)?$', target)
        if bridge:
            return f'[{label}](files/code/bridge-{bridge.group(1)}{bridge.group(2) or "/"})'
        if target in TARGET:
            folder, name, anchor = TARGET[target]
            if name.startswith('files/'):
                return f'[{label}]({name})'
            anchor = anchor or frag
            if folder == here and name == page:
                return f'[{label}](#{anchor})' if anchor else f'[{label}](#)'
            rel = name if folder == here else f'../{folder}/{name}'
            return f'[{label}]({rel}{"#" + anchor if anchor else ""})'
        if target.endswith('README.md') and target.count('/') <= 1:
            return f'[{label}](index.md)' if here == 'episodes' else f'[{label}](../index.md)'
        print('  unmapped link in', src_rel, '->', url)
        return m.group(0)
    return re.sub(r'(?<!!)\[([^\]]*)\]\(([^)\s]+)\)', fix, t)


def placeholders(t):
    return re.sub(r'assets/images/week-\d/([\w.-]+\.png)', r'episodes/fig/\1', t)


def drop_nav(t):
    t = re.sub(r'^\[<< Back to[^\n]*\n?', '', t, flags=re.M)
    t = re.sub(r'^\[Back to[^\n]*\n?', '', t, flags=re.M)
    return t


def strip_section_header(t):
    """Remove title, week line, back link and Contents list from a lesson section."""
    lines = t.split('\n')
    i = 0
    while i < len(lines) and not lines[i].startswith('## Contents'):
        i += 1
    i += 1
    while i < len(lines) and (lines[i].strip() == '' or lines[i].lstrip().startswith('- [')):
        i += 1
    body = '\n'.join(lines[i:])
    return re.sub(r'^# Section [\d.]+\s*\n', '', body, flags=re.M)   # stray H1s


def strip_title(t):
    return re.sub(r'^# [^\n]*\n', '', t, count=1)


def challenges(t):
    """Wrap the exercises section in Workbench challenge blocks."""
    m = re.search(r'^## (?:💻 )?Exercises[^\n]*\n', t, flags=re.M)
    if not m:
        return t
    head, ex = t[:m.start()], t[m.end():]
    ex = re.sub(r'^\*\*(Level \d[^*\n]*)\*\*[ \t]*$', r'### \1', ex, flags=re.M)   # bold level labels
    parts = re.split(r'^### (Exercises?:? ?Level \d|Level \d)[^\n]*\n', ex, flags=re.M)
    blocks = []
    if len(parts) == 1:
        blocks.append(('Exercises', parts[0]))
    else:
        if parts[0].strip():
            blocks.append(('Exercises', parts[0]))
        for k in range(1, len(parts), 2):
            name = re.sub(r'^Exercises?:? ?', '', parts[k]).strip()
            blocks.append((f'Exercises: {name}', parts[k + 1]))
    out = head.rstrip() + '\n\n'
    for title, body in blocks:
        out += f'::::::::::::::::::::::::::::::::::::: challenge\n\n## {title}\n\n{body.strip()}\n\n::::::::::::::::::::::::::::::::::::::::::::::::\n\n'
    return out


def bridge_blocks(t):
    """Turn 'Activity' + following 'Model answer' sections into a challenge with a solution."""
    m = re.search(r'^## (Activit[^\n]*)\n(.*?)^## (Model answers?[^\n]*)\n(.*?)(?=^## |\Z)', t, flags=re.M | re.S)
    if not m:
        return t
    block = (f'::::::::::::::::::::::::::::::::::::: challenge\n\n## {m.group(1)}\n\n{m.group(2).strip()}\n\n'
             f':::::::::::::::: solution\n\n## {m.group(3)}\n\n{m.group(4).strip()}\n\n:::::::::::::::::::::::::\n'
             f'::::::::::::::::::::::::::::::::::::::::::::::::\n\n')
    return t[:m.start()] + block + t[m.end():]


def demote(t, levels=1):
    """Push every markdown heading down `levels` levels (outside code blocks), so that only the
    week page's own level-2 headings appear in the Workbench menu."""
    out, fence = [], None
    for line in t.split('\n'):
        f = re.match(r'^\s*(```+|~~~+)', line)
        if f:
            fence = None if fence and f.group(1).startswith(fence[:3]) else (fence or f.group(1))
        elif fence is None:
            h = re.match(r'^(#{1,5}) ', line)
            if h:
                line = '#' * min(6, len(h.group(1)) + levels) + line[len(h.group(1)):]
        out.append(line)
    return '\n'.join(out)


def box(kind, items):
    body = '\n'.join(f'- {x}' for x in items)
    return f':::::::::::::::::::::::::::::::::::::: {kind}\n\n{body}\n\n::::::::::::::::::::::::::::::::::::::::::::::::\n'


def clean(t, src_rel, here, page):
    return placeholders(links(fences(drop_nav(t)), src_rel, here, page)).strip() + '\n'


def read(rel):
    with open(os.path.join(SRC, rel), encoding='utf-8') as f:
        return f.read()


def write(folder, name, text):
    path = os.path.join(DST, folder, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def part(title, anchor, body):
    return f'## {title} {{#{anchor}}}\n\n{body.strip()}\n\n'


# ---------------------------------------------------------------- build
os.makedirs(EP, exist_ok=True)
for f in os.listdir(EP):          # remove episodes from earlier conversions
    if f.endswith('.md'):
        os.remove(os.path.join(EP, f))
for sub in ('files', 'data'):     # remove generated files, so renamed or deleted ones do not linger
    shutil.rmtree(os.path.join(EP, sub), ignore_errors=True)
    os.makedirs(os.path.join(EP, sub), exist_ok=True)

order = []
for w, theme in WEEKS.items():
    watch, rp, bridge_min, build = TIME[w]
    secs = [s for s in SECTIONS if s.startswith(f'{w}.')]
    page = week_file(w)
    body = ''

    # overview
    rel = f'weeks/week-{w}/README.md'
    t = clean(strip_title(read(rel)), rel, 'episodes', page)
    t = re.sub(r'^## (Next week|What comes next)\n.*', '', t, flags=re.M | re.S)   # the menu already links the next week
    body += part(f'Week {w} overview', f'week-{w}-overview', demote(t))

    # sections
    for s in secs:
        m = SECTIONS[s]
        src = 'weeks/' + m['src']
        t = challenges(clean(strip_section_header(read(src)), src, 'episodes', page))
        body += part(f"{s} {m['title']}", sec_anchor(s), demote(t))

    # bridge
    rel = f'weeks/week-{w}/bridge.md'
    t = bridge_blocks(clean(strip_title(read(rel)), rel, 'episodes', page))
    body += part(f"Concepts Bridge: {BRIDGES[w]['title']}", f'week-{w}-bridge', demote(t))

    # practice
    pm = PRACTICE[w]
    rel = f'weeks/week-{w}/practice/README.md'
    t = clean(strip_title(read(rel)), rel, 'episodes', page)
    files = '\n'.join(f'- [{f}](files/{"week-" + str(w)}/{f})' for f in pm['files'])
    t = (':::::::::::::::::::::::::::::::::::::::: callout\n\n## Files for this task\n\n'
         'The easiest way to get every file is the [course zip file](data/course-data.zip) from the Setup page. '
         'Unzip it and open the folder in PyCharm. The programs find the data files by their place in that folder, '
         'so keep the folder layout. You can also download single files here:\n\n'
         f'{files}\n\n:::::::::::::::::::::::::::::::::::::::::::::::::::\n\n') + t
    t = demote(t)
    title = pm['title'].replace('Practice: ', '')
    body += part(f'Practice task: {title}', f'week-{w}-practice', t)

    # page metadata: the week's questions, objectives and key points
    q = [f'What will I learn in Week {w}, and how should I spend my 6 hours?']
    o = ['Plan your study time for the week using the time plan.']
    k = ['Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.']
    for s in secs:
        q += SECTIONS[s]['q']; o += SECTIONS[s]['o']; k += SECTIONS[s]['k']
    q += BRIDGES[w]['q']; o += BRIDGES[w]['o']; k += BRIDGES[w]['k']
    pq, po, pk = PRACTICE_Q[w]
    q += pq; o += po; k += pk
    head = (f"---\ntitle: 'Week {w}: {theme}'\nteaching: {watch + round(rp * 0.6) + 20}\n"
            f"exercises: {round(rp * 0.4) + 10 + build}\n---\n\n")
    write('episodes', page, head + box('questions', q) + '\n' + box('objectives', o) + '\n' + body.strip() + '\n\n' + box('keypoints', k))
    order.append(page)
    for f in pm['files']:
        dst = os.path.join(EP, 'files', f'week-{w}', f)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(os.path.join(W, f'week-{w}', 'practice', f), dst)

# lesson code folders (e.g. 2.1_code) -> episodes/files/code/2.1/, and bridge code -> files/code/bridge-N/
IGNORE = shutil.ignore_patterns('__pycache__', '*.pyc', '.pytest_cache')
for w in WEEKS:
    lessons = os.path.join(W, f'week-{w}', 'lessons')
    for d in os.listdir(lessons):
        if d.endswith('_code'):
            shutil.copytree(os.path.join(lessons, d), os.path.join(EP, 'files', 'code', d[:-5]), ignore=IGNORE, dirs_exist_ok=True)
    bridge_code = os.path.join(W, f'week-{w}', 'bridge_code')
    if os.path.isdir(bridge_code):
        shutil.copytree(bridge_code, os.path.join(EP, 'files', 'code', f'bridge-{w}'), ignore=IGNORE, dirs_exist_ok=True)

# data and example files
for sub in ('data', 'files'):
    src = os.path.join(SRC, 'assets', sub)
    for f in os.listdir(src):
        shutil.copyfile(os.path.join(src, f), os.path.join(EP, sub, f))

# one zip that keeps the course folder layout (assets/ and weeks/week-N/...), so every program finds its data
with zipfile.ZipFile(os.path.join(EP, 'data', 'course-data.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
    for sub in ('data', 'files'):
        for f in sorted(os.listdir(os.path.join(SRC, 'assets', sub))):
            z.write(os.path.join(SRC, 'assets', sub, f), f'{ZIP_ROOT}/assets/{sub}/{f}')
    for w in WEEKS:
        base = os.path.join(W, f'week-{w}')
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = sorted(d for d in dirnames if d not in ('__pycache__', '.pytest_cache'))
            for f in sorted(filenames):
                if f.endswith(('.py', '.txt')):
                    full = os.path.join(dirpath, f)
                    rel = os.path.relpath(full, SRC).replace(os.sep, '/')
                    z.write(full, f'{ZIP_ROOT}/{rel}')

print(len(order), 'week episodes')
print('episodes:', ' '.join(order))
