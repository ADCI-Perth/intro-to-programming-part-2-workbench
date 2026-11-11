---
title: 'Week 2: Files and structured data'
teaching: 120
exercises: 172
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 2, and how should I spend my 6 hours?
- How do I read from and write to a file?
- What happens when the file is not there?
- How do I read and write tables stored as text?
- How do I save nested data such as dictionaries and lists?
- What is in a web-server log line?
- How do I take one line apart?
- Why must I check data that comes from outside my program?
- Can I turn a raw log into a CSV file, and keep my library between runs?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Open files safely with with and encoding="utf-8".
- Read a file all at once and line by line.
- Handle FileNotFoundError.
- Read rows with csv.reader and csv.DictReader.
- Write rows with csv.writer and csv.DictWriter.
- Save and load JSON with json.dump and json.load.
- Turn an object into a dictionary before saving it.
- Name the parts of a log line.
- Explain the status codes 200, 304, 401, 404 and 500.
- Split a log line into its parts.
- Explain why data from a file or download may be wrong or hostile.
- Explain why JSON and CSV are safer to load than pickle files or eval().
- Convert a web log to CSV, and add save and load to your Part 1 library.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 2 overview {#week-2-overview}

**Theme:** read and write text files, CSV and JSON, take a web log apart line by line, and save your library so it survives between runs.

**What you need from earlier weeks:** strings, `split`, `strip` and f-strings from Week 1, and your own `library.py` and `main.py` from Part 1 Week 6.

### Learning goals

By the end of this week you can:

1. Open, read and write text files safely with `with` and `encoding="utf-8"`.
2. Read and write CSV files with the `csv` module, and JSON files with the `json` module.
3. Take a web-server log line apart and explain the common status codes.
4. Explain why data from outside must be checked before you trust it, and why JSON and CSV are safer than `pickle` or `eval`.

### Time plan (under 6 hours)

| Block | Time | What you do |
|---|---|---|
| Watch | 37 min | Three videos (below) |
| Read & practise | 1 h 45 min | Sections 2.1 to 2.4, with Level 1 exercises |
| Concepts Bridge | 30 min | [Trusting data from outside](#week-2-bridge) |
| Build | 2 h | [Web-log converter, and save and load for the library](#week-2-practice), your portfolio item for this week |
| Quiz | 15 min | Canvas quiz, 6 questions |
| **Total** | **5 h 7 min** | Under the 6 h cap |

### Watch (37 min)

Watch these in order. Pause and try the code yourself in PyCharm. The videos are from different presenters, so the style changes from video to video.

| # | Video | Length | Look out for |
|---|---|---|---|
| 1 | [Visually Explained] [Python File Handling - Visually Explained](https://www.youtube.com/watch?v=PXySDMxOPnI) | 14:15 | How to open a file, the modes for reading and writing, and why `with` closes the file for you. |
| 2 | [Corey Schafer] [Python Tutorial: CSV Module - How to Read, Parse, and Write CSV Files](https://www.youtube.com/watch?v=q5uM4VKywbA) | 16:11 | How the `csv` module reads and writes rows, as lists and as dictionaries. |
| 3 | [Tech With Tim] [How To Use JSON In Python](https://www.youtube.com/watch?v=-51jxlQaxyA) | 6:11 | How JSON text becomes Python data, and how Python data becomes JSON text. |

**Total: 36 min 37 s, shown as 37 min.**

### Read & practise (1 h 45 min)

Open each lesson, read it, type out the examples and run them. Do not just copy and paste. Do the **Level 1** exercises at the end of each section.

#### Section 2.1: Text files (about 35 min)

Lesson: [Section 2.1: Text files](#section-2-1). Code: [lessons/2.1_code/](files/code/2.1/).

- Read: `with`, the modes `"r"`, `"w"` and `"a"`, reading and looping, `FileNotFoundError`, and file paths.
- Do Level 1 exercises 1 to 6.

**PyCharm note:** your scripts create files next to themselves. They appear in the Project panel after you run the script. Press the refresh arrow if you do not see them.

#### Section 2.2: CSV files (about 30 min)

Lesson: [Section 2.2: CSV files](#section-2-2). Code: [lessons/2.2_code/](files/code/2.2/).

- Read: `csv.reader`, `csv.DictReader`, `csv.writer`, `csv.DictWriter`, `newline=""`, and why everything is a string.
- Do Level 1 exercises 1 to 6.

#### Section 2.3: JSON (about 25 min)

Lesson: [Section 2.3: JSON](#section-2-3). Code: [lessons/2.3_code/](files/code/2.3/).

- Read: `dump`, `load`, `dumps`, `loads`, what JSON can hold, and why an object becomes a dictionary first.
- Do Level 1 exercises 1 to 6.

#### Section 2.4: Reading a web log line by line (about 15 min)

Lesson: [Section 2.4: Reading a web log](#section-2-4). Code: [lessons/2.4_code/](files/code/2.4/).

- Read: the parts of a log line, the status codes, and how to take one line apart.
- Do Level 1 exercises 1 to 6. Keep them short.

The section times add up to 35 + 30 + 25 + 15 = 105 minutes, which is 1 h 45 min.

### Concepts Bridge (30 min)

Go to [bridge.md](#week-2-bridge). It explains why data from a file, download or form must be checked, and why `pickle.load` and `eval()` can run code while JSON and CSV cannot. It has two short activities.

### Build (2 h)

Go to [practice/README.md](#week-2-practice). In Part A (about 60 min) you build a converter that turns the web log into a CSV file. In Part B (about 45 min) you add `to_dict`, `from_dict`, `save` and `load` to your library, so your books are kept between runs. The last 15 minutes are for tidying, tests and a short written note. This is your portfolio item for Week 2.

### Quiz (15 min)

Take the Canvas quiz for Week 2 after you finish the Build. It has 6 questions, drawn from a pool. It is marked automatically.

### Portfolio this week

Submit at the end of the week, in your portfolio folder:

- `log_converter.py` (your web-log converter)
- `web_log.csv` (the file your converter wrote)
- `library.py` (your library with `to_dict`, `from_dict`, `save` and `load`)
- `main.py` (your menu program, which loads and saves)
- `data_note.txt` (five or six sentences, see the practice task)

Your tutor marks the portfolio. The quiz is marked automatically.

### Optional

Only if you have time and are curious.

- Sections 2.1 to 2.4 Level 2 exercises.
- Python Software Foundation (2026) *csv — CSV File Reading and Writing*. Available at: https://docs.python.org/3/library/csv.html (Accessed: 11 November 2026).
- Python Software Foundation (2026) *json — JSON encoder and decoder*. Available at: https://docs.python.org/3/library/json.html (Accessed: 11 November 2026).
- Python Software Foundation (2026) *pathlib — Object-oriented filesystem paths*. Available at: https://docs.python.org/3/library/pathlib.html (Accessed: 11 November 2026).

---

## 2.1 Text files {#section-2-1}

### Why files matter

So far your programs forget everything when they stop. Files fix that. A program can save its results in a file and read them back later.

Files are also where most data lives. Web servers write a log file of every request. A security analyst reads those files to find odd behaviour. In this section you learn the basic steps: open a file, read or write it, and close it.

A **text file** holds characters, such as letters, digits and spaces. You can open it in PyCharm and read it. It ends in `.txt` or `.log`. In Week 1 you learned that characters are stored as bytes using an **encoding**. We use UTF-8 every time.

Code for this section: [2.1_code/text_files.py](files/code/2.1/text_files.py). Type the examples yourself first.

### Open a file with `with`

The built-in function `open` gives you access to a file. The safe way to use it is a `with` block:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    text = file.read()
```

Take it apart:

- `open(...)` needs the **file name** first.
- The second value is the **mode**, which says what you want to do (see the table below).
- `encoding="utf-8"` tells Python how to turn bytes into characters. Always write it.
- `as file` gives the open file a name. You can pick any name.
- The indented lines are the **block**. When the block ends, Python closes the file for you, even if an error happens. A file left open can lose data, so always use `with`.

| Mode | Meaning | If the file exists | If it does not exist |
|---|---|---|---|
| `"r"` | read (the default) | reads it | `FileNotFoundError` |
| `"w"` | write | **empties it first** | creates it |
| `"a"` | append (add to the end) | keeps it, adds to the end | creates it |

Be careful with `"w"`. It wipes the old contents as soon as the file is opened.

### Write a file

Use the `write` method. It writes exactly the text you give it. It does **not** add a new line, so put `\n` at the end of each line.

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Checked the backup at 9 am.\n")
    file.write("Two failed logins from 203.0.113.45.\n")
```

Run it. A new file called `notes.txt` appears next to your script. (The full example saves it next to the script file. See [File paths](#file-paths).)

### Read a whole file

`read()` returns the whole file as one string.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text)
print(len(text), "characters")
```

```output
Checked the backup at 9 am.
Two failed logins from 203.0.113.45.

65 characters
```

There is an empty line after the text. The file ends with `\n`, and `print` adds another one. Whole-file reading is fine for small files. For big logs, read line by line.

### Read line by line

A file is **iterable**, so a `for` loop gives you one line at a time. This works for a file of any size, because Python does not hold it all in memory.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(repr(line))
```

```output
'Checked the backup at 9 am.\n'
'Two failed logins from 203.0.113.45.\n'
```

`repr` shows the hidden characters. Every line still ends with `\n`, the **newline** character. Use `strip()` (from Week 1) to remove it:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

```output
Checked the backup at 9 am.
Two failed logins from 203.0.113.45.
```

To keep the lines, add them to a list:

```python
lines = []
with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.strip())
```

### Add to a file

Mode `"a"` keeps what is already there and adds to the end:

```python
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("Rang the café about the router.\n")
```

The file now has three lines. Because you used UTF-8, the `é` is saved and read back correctly.

### When the file is not there

If you open a missing file for reading, Python raises `FileNotFoundError`. You met `try` and `except` in Part 1. Use them here:

```python
try:
    with open("no_such_file.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Cannot find no_such_file.txt")
```

```output
Cannot find no_such_file.txt
```

The program carries on instead of crashing. Catch this one error, not every error, so that you do not hide other problems.

### File paths

A **path** says where a file is. Python looks for a plain name like `"notes.txt"` in the **working folder**, which is not always where your script is. In PyCharm it depends on how you ran the file. This causes many "file not found" surprises.

A safer way is to build the path from the script's own location. Python's `pathlib` module does this. Here is the line, ready-made. Use it as it is:

```python
from pathlib import Path

HERE = Path(__file__).parent
notes_file = HERE / "notes.txt"
```

- `__file__` is the path of the script that is running.
- `.parent` is the folder that holds it.
- The `/` joins a folder and a file name. It works on Windows, Mac and Linux.
- A `Path` can be given straight to `open`.

Some handy parts of a path:

```python
print(HERE.name)             # the folder's name
print(notes_file.name)       # notes.txt
print(notes_file.exists())   # True or False
```

Note: `Path(__file__)` works when you run a file. It does not work if you type code in the Python console.

### Common mistakes

- **Using `"w"` when you meant `"a"`.** This erases the old contents. Check the mode.
- **Forgetting `\n`.** `write` does not start a new line for you. Two writes without `\n` join into one line.
- **Leaving out `encoding="utf-8"`.** On some computers, text with `é` then reads back wrongly.
- **Forgetting `strip()`.** A line read from a file ends with `\n`, so `line == "yes"` is false for `"yes\n"`.
- **Writing a number.** `file.write(5)` is a `TypeError`. Use `file.write(str(5))` or an f-string.
- **Reading after the block ends.** The file is closed when the `with` block ends. Do all the file work inside it.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Write a file `shopping.txt` with three items, one per line. Use `write` and `\n`.
2. Read `shopping.txt` and print each item with `strip()`, with its number first (`1. milk`). Use `enumerate` or a counter.
3. Add a fourth item with mode `"a"`. Read the file again and print how many lines it has.
4. Read `shopping.txt` into a list. Print the list in reverse order.
5. Write a function `count_lines(path)` that returns the number of lines in a file. If the file is missing, return `0`. Test it with a file that exists and one that does not.
6. Use `Path(__file__).parent` to build the path of `shopping.txt`, so that your script finds it however you run it.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Write `longest_line(path)` that returns the longest line in a file (without the newline).
2. Copy one text file into a new file, changing every line to upper case.
3. Write a small program that asks for a note with `input()` and adds it to `notes.txt` each time you run it, with the number of the note at the start.

[Next: Section 2.2, CSV files](#section-2-2)

::::::::::::::::::::::::::::::::::::::::::::::::

## 2.2 CSV files {#section-2-2}

### Why CSV

**CSV** stands for comma-separated values. It is a text file that holds a table. Each line is a row. The values in a row are separated by commas. The first row is usually the **header**, which names the columns.

```output
user,office,logins
user01,"Perth, WA",14
user02,"Fremantle, WA",3
```

Spreadsheets, databases and security tools all export CSV. In Week 5 you will read CSV with Pandas. First you learn the `csv` module that comes with Python.

Code for this section: [2.2_code/csv_files.py](files/code/2.2/csv_files.py).

### Write a CSV file

`csv.writer` turns lists into CSV lines. `writerow` writes one row. `writerows` writes a list of rows.

```python
import csv

rows = [
    ["user01", "Perth, WA", 14],
    ["user02", "Fremantle, WA", 3],
    ["user03", "Joondalup, WA", 27],
]

with open("logins.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["user", "office", "logins"])
    writer.writerows(rows)
```

Open `logins.csv` to see what was written:

```output
user,office,logins
user01,"Perth, WA",14
user02,"Fremantle, WA",3
user03,"Joondalup, WA",27
```

The module added quote marks around `Perth, WA`, because that value has a comma in it. It also turned the numbers into text for you.

### Why not just split on commas

You could try `line.split(",")`. It fails when a value contains a comma:

```python
line = 'user01,"Perth, WA",14'
print(line.split(","))
```

```output
['user01', '"Perth', ' WA"', '14']
```

That is four pieces, not three, and the quote marks are left in. The `csv` module understands the quotes. Always use it for CSV, even when your data looks simple today.

### Read with `csv.reader`

`csv.reader` gives you each row as a list of strings.

```python
with open("logins.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

```output
['user', 'office', 'logins']
['user01', 'Perth, WA', '14']
['user02', 'Fremantle, WA', '3']
['user03', 'Joondalup, WA', '27']
```

The header is the first row. You get it like any other row, so skip it if you only want the data. You find values by position: `row[2]`.

### Read with `csv.DictReader`

`csv.DictReader` uses the header row for you. Each row is a **dictionary**, so you find values by column name. This is easier to read and does not break if the columns move.

```python
total = 0
with open("logins.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["user"], row["logins"])
        total = total + int(row["logins"])

print("Total logins:", total)
```

```output
user01 14
user02 3
user03 27
Total logins: 44
```

### Everything is a string

A CSV file holds only text. The reader cannot know that `14` is a number. Every value comes back as a string.

```python
with open("logins.csv", "r", newline="", encoding="utf-8") as file:
    records = list(csv.DictReader(file))

print(records[0])
print(records[0]["logins"] + records[1]["logins"])
print(int(records[0]["logins"]) + int(records[1]["logins"]))
```

```output
{'user': 'user01', 'office': 'Perth, WA', 'logins': '14'}
143
17
```

Adding two strings joins them (`"14" + "3"` is `"143"`). Convert with `int()` or `float()` before you do sums. An empty cell is `""`, and `int("")` raises `ValueError`, so check for it first when a column can be empty.

### Write with `csv.DictWriter`

`csv.DictWriter` writes dictionaries. You give it the column names with `fieldnames`. `writeheader()` writes the header row. `writerow` and `writerows` write the data.

```python
busy = []
for record in records:
    if int(record["logins"]) >= 10:
        busy.append({"user": record["user"], "logins": record["logins"]})

with open("summary.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["user", "logins"])
    writer.writeheader()
    writer.writerows(busy)
```

```output
user,logins
user01,14
user03,27
```

Every key in each dictionary must be in `fieldnames`, or Python raises `ValueError`. A key that is missing from a dictionary gives an empty cell.

### Why `newline=""`

When you open a CSV file, add `newline=""`. The `csv` module manages line endings itself. Without this, on Windows you can get a blank line between every row in the file you write. The reader can also misread a value that has a line break inside quotes. Add it when you read and when you write.

### Common mistakes

- **Using `split(",")`.** It breaks on commas inside quotes. Use the `csv` module.
- **Forgetting `newline=""`.** You may get blank lines in your output on Windows.
- **Doing sums on strings.** `"14" + "3"` is `"143"`. Convert first.
- **Forgetting the header row.** With `csv.reader`, the first row is the header. With `DictReader`, it is used for the keys and is not in the data.
- **Reading the file twice from one reader.** A reader can be looped over only once. Make a list with `list(reader)` if you need the rows again.
- **Wrong `fieldnames`.** The names must match the dictionary keys exactly, including case.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Use `csv.writer` to write `pets.csv` with the header `name,kind,age` and three rows of your own.
2. Read `pets.csv` with `csv.reader` and print each row. Then change the code to skip the header.
3. Read `pets.csv` with `csv.DictReader`. Print `name is N years old` for each pet. Convert the age with `int()`.
4. Work out the average age of your pets. Print it with one decimal place.
5. Write `old_pets.csv` with `csv.DictWriter`. Include only pets older than 3. Keep the same header.
6. Add a pet whose name has a comma, such as `Rex, Jr`. Open the file in PyCharm and say what you see around the name.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Write `read_table(path)` that returns a list of dictionaries. Test it on `pets.csv`.
2. Write `column_total(records, column)` that adds up one numeric column. Return `0` for no records.
3. Make a CSV file where one row has an empty age. Change your average code so it skips the empty values.

[Next: Section 2.3, JSON](#section-2-3)

::::::::::::::::::::::::::::::::::::::::::::::::

## 2.3 JSON {#section-2-3}

### Why JSON

CSV holds a flat table. Many things are not flat. A device might have a name, an address and a *list* of open ports. **JSON** (JavaScript Object Notation) holds nested data like that. Web services, configuration files and security tools all use it.

JSON is a text format. Every programming language can read it, so it is a good way to hand data from one program to another.

Code for this section: [2.3_code/json_files.py](files/code/2.3/json_files.py).

### What JSON looks like

JSON looks very much like Python dictionaries and lists:

```output
{
  "name": "front-desk-pc",
  "address": "192.0.2.15",
  "ports": [80, 443],
  "patched": true,
  "owner": null
}
```

The differences are small but they matter:

- Text uses **double quotes only**. Single quotes are not valid JSON.
- `true` and `false` are lower case. Python has `True` and `False`.
- `null` means "nothing". Python has `None`.
- No comma after the last item.

The `json` module does the changes for you. Start with `import json`.

### Strings: `dumps` and `loads`

The `s` in these names stands for *string*.

- `json.dumps(value)` turns a Python value into a JSON string.
- `json.loads(text)` turns a JSON string into a Python value.

```python
import json

device = {
    "name": "front-desk-pc",
    "address": "192.0.2.15",
    "ports": [80, 443],
    "patched": True,
    "owner": None,
}

text = json.dumps(device)
print(text)
print(type(text))
```

```output
{"name": "front-desk-pc", "address": "192.0.2.15", "ports": [80, 443], "patched": true, "owner": null}
<class 'str'>
```

`True` became `true` and `None` became `null`. Add `indent=2` to lay it out for people to read:

```python
print(json.dumps(device, indent=2))
```

```output
{
  "name": "front-desk-pc",
  "address": "192.0.2.15",
  "ports": [
    80,
    443
  ],
  "patched": true,
  "owner": null
}
```

Now go the other way:

```python
incoming = '{"user": "user01", "attempts": 3, "locked": false}'
record = json.loads(incoming)
print(record)
print(record["attempts"] + 1)
print(type(record["locked"]))
```

```output
{'user': 'user01', 'attempts': 3, 'locked': False}
4
<class 'bool'>
```

Unlike CSV, JSON keeps numbers as numbers and `true` as a real boolean.

### Files: `dump` and `load`

Without the `s`, the functions work with files.

- `json.dump(value, file)` writes a Python value into an open file.
- `json.load(file)` reads a Python value from an open file.

```python
with open("device.json", "w", encoding="utf-8") as file:
    json.dump(device, file, indent=2)

with open("device.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

print(loaded["name"])
print(loaded["ports"])
print(loaded == device)
```

```output
front-desk-pc
[80, 443]
True
```

The value came back equal to the original. Note that you do not need `newline=""` for JSON, only for CSV.

A quick way to remember: `dump`/`load` use a file, `dumps`/`loads` use a string.

### What JSON can hold

| Python | JSON |
|---|---|
| `dict` (with string keys) | object `{}` |
| `list`, `tuple` | array `[]` |
| `str` | string |
| `int`, `float` | number |
| `True`, `False` | `true`, `false` |
| `None` | `null` |

Things do not always come back the same. A tuple becomes a list, and a number used as a dictionary key becomes a string:

```python
changed = json.loads(json.dumps({"point": (3, 4), 200: "OK"}))
print(changed)
```

```output
{'point': [3, 4], '200': 'OK'}
```

Sets, and your own objects, are not on the list. JSON cannot hold them.

### Bad JSON

If the text is not valid JSON, `json.loads` raises `json.JSONDecodeError`. Catch it when the text comes from outside your program:

```python
try:
    json.loads("{'user': 'user01'}")
except json.JSONDecodeError:
    print("That text is not valid JSON.")
```

```output
That text is not valid JSON.
```

Single quotes are not valid, so this fails. Valid JSON can still be wrong for your program, for example a missing key. The Concepts Bridge this week looks at checking what you load.

### Objects must become dictionaries first

JSON cannot store a class object. This is a `TypeError`:

```python
class Device:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def to_dict(self):
        return {"name": self.name, "address": self.address}


printer = Device("printer-2", "192.0.2.40")

try:
    json.dumps(printer)
except TypeError as error:
    print("TypeError:", error)
```

```output
TypeError: Object of type Device is not JSON serializable
```

The fix is to turn the object into a dictionary first. Give the class a `to_dict` method. A dictionary of simple values is something JSON can store.

```python
print(json.dumps(printer.to_dict()))

devices = [printer, Device("scanner-1", "192.0.2.41")]
print(json.dumps([d.to_dict() for d in devices], indent=2))
```

```output
{"name": "printer-2", "address": "192.0.2.40"}
[
  {
    "name": "printer-2",
    "address": "192.0.2.40"
  },
  {
    "name": "scanner-1",
    "address": "192.0.2.41"
  }
]
```

You will use this idea in the Build to save your library's books.

### Common mistakes

- **Mixing up `dump` and `dumps`.** `dump` needs a file. `dumps` gives a string.
- **Single quotes.** `{'a': 1}` is a Python dictionary, not JSON.
- **Expecting tuples or number keys to come back unchanged.** They change type.
- **Trying to save an object.** Use a method like `to_dict` first.
- **Forgetting `encoding="utf-8"`.** Use it with JSON files too.
- **Trusting the shape.** A file can be valid JSON and still lack the keys you expect.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Make a dictionary for a person with `"name"`, `"age"` and a list of `"hobbies"`. Use a made-up name such as Jack Wilson. Print `json.dumps(person, indent=2)`.
2. Save the dictionary to `person.json` with `json.dump`, then load it back with `json.load`. Print the second hobby.
3. Use `json.loads` on the string `'{"ok": true, "count": 5}'`. Print `count * 2` and the type of `ok`.
4. Without running it, say what `json.dumps([True, None, "hi"])` gives. Then run it to check.
5. Write a `try`/`except` that loads the text `"{name: 1}"` and prints a friendly message when it is not valid JSON.
6. Write a class `Note` with `text` and `urgent`, and a `to_dict` method. Save a list of two notes to `notes.json`.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Load `notes.json` back and build a list of `Note` objects. (You will do this properly with `from_dict` in the Build.)
2. Make a dictionary with a tuple value. Send it through `dumps` and `loads`. Write down what changed.
3. Write `load_or_default(path, default)` that returns the loaded JSON, or `default` when the file is missing.

[Next: Section 2.4, Reading a web log](#section-2-4)

::::::::::::::::::::::::::::::::::::::::::::::::

## 2.4 Reading a web log line by line {#section-2-4}

### Why logs matter

A web server writes one line to a **log file** for every request it receives. A log is a record of what happened. When something goes wrong, or someone behaves oddly, the log is the first place to look. A person cannot read thousands of lines, so a program reads them.

The log in this course is **synthetic**. It was made up for learning. It has 200 lines, and the addresses come from ranges reserved for examples. It is in `assets/files/web_log.txt` in the course folder.

Code for this section: [2.4_code/web_log.py](files/code/2.4/web_log.py).

### What is in a log line

Here is the first line of the file:

```output
192.0.2.33 - - [09/Nov/2026:07:13:45 +0800] "GET /contact.html HTTP/1.1" 200 2260
```

| Part | Example | Meaning |
|---|---|---|
| Address | `192.0.2.33` | The **IP address** of the computer that made the request |
| Two dashes | `- -` | Two fields this log does not use |
| Time | `[09/Nov/2026:07:13:45 +0800]` | Date, time, and the time zone offset |
| Request | `"GET /contact.html HTTP/1.1"` | The method, the page asked for (the path), and the protocol |
| Status code | `200` | The server's answer |
| Size | `2260` | The size of the answer in bytes, or `-` when there is none |

`GET` means "give me this page". `POST` means "here is some data", for example a login form.

### Status codes

The status code is a three-digit number. Five appear in our log:

| Code | Meaning |
|---|---|
| `200` | OK. The page was sent. |
| `304` | Not modified. The browser already has the latest copy, so nothing was sent (this is why the size is `-`). |
| `401` | Unauthorised. A login was needed or the login failed. |
| `404` | Not found. The page asked for does not exist. |
| `500` | Server error. The server failed to do its job. |

Many `401` answers to one address, or many `404` answers for odd pages, can be a sign that someone is probing the site. You will count them in the Build.

### Take one line apart

The parts are separated by spaces, so `split()` with no argument cuts the line into pieces. Use `strip` to remove the `[` and the quote marks that stick to the pieces.

```python
line = '192.0.2.33 - - [09/Nov/2026:07:13:45 +0800] "GET /contact.html HTTP/1.1" 200 2260'

parts = line.split()
print(len(parts))
print(parts)
```

```output
10
['192.0.2.33', '-', '-', '[09/Nov/2026:07:13:45', '+0800]', '"GET', '/contact.html', 'HTTP/1.1"', '200', '2260']
```

There are 10 parts. Count from zero:

| Position | Value |
|---|---|
| `parts[0]` | the IP address |
| `parts[3]` | the date and time, with a `[` at the start |
| `parts[5]` | the method, with a `"` at the start |
| `parts[6]` | the path |
| `parts[8]` | the status code |
| `parts[9]` | the size, or `-` |

```python
ip = parts[0]
stamp = parts[3].strip("[")
method = parts[5].strip('"')
path = parts[6]
status = parts[8]
size = parts[9]

print(ip)
print(stamp)
print(method)
print(path)
print(status, size)
```

```output
192.0.2.33
09/Nov/2026:07:13:45
GET
/contact.html
200 2260
```

`strip("[")` removes a `[` from either end of the string. `strip('"')` does the same for a quote mark. Notice that `status` is still a string. Use `int(status)` if you need a number.

### Split the date from the time

`stamp` holds the date and time joined by colons. Split on `:` to separate them. The date is the first piece. The time is the other three, which you join back with `":"`.

```python
pieces = stamp.split(":")
print(pieces)
date = pieces[0]
time = ":".join(pieces[1:])
print(date)
print(time)
```

```output
['09/Nov/2026', '07', '13', '45']
09/Nov/2026
07:13:45
```

### Read the real log

Now read the whole file, as in Section 2.1. The path is built from `Path(__file__)`. The lesson file is four folders below the course folder, so `parents[4]` reaches the course folder. If you keep the file somewhere else, set `log_file` to the right path yourself.

```python
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[4] / "assets"
log_file = ASSETS / "files" / "web_log.txt"

total = 0
not_found = 0
with open(log_file, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.split()
        if len(parts) < 10:
            continue
        total = total + 1
        if parts[8] == "404":
            not_found = not_found + 1

print(total, "lines")
print(not_found, "with status 404")
```

```output
200 lines
16 with status 404
```

`continue` skips to the next line. The check `len(parts) < 10` protects you from a blank or damaged line, which would otherwise cause an `IndexError`. Real logs often have bad lines, so always check.

One more fact: lines whose status is `304` have `-` as the size.

```output
198.51.100.48 - - [09/Nov/2026:12:04:23 +0800] "GET /index.html HTTP/1.1" 304 -
```

### Common mistakes

- **Counting from one.** `parts[0]` is the first part.
- **Not removing `[` and `"`.** `'"GET'` is not equal to `'GET'`.
- **Forgetting the size can be `-`.** `int("-")` is a `ValueError`. Check for `-` first.
- **No check for short lines.** A blank line gives an empty list, and `parts[8]` fails.
- **Comparing the status to a number.** `parts[8] == 404` is false, because `parts[8]` is the string `"404"`.
- **Wrong path.** If the file is not found, check the `parents[...]` number or the folder you are in.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Split this line and print the IP address, the path and the status: `198.51.100.23 - - [09/Nov/2026:07:22:54 +0800] "GET /images/logo.png HTTP/1.1" 200 18240`
2. For the same line, print the date and the time as two separate values.
3. Print the first five lines of `web_log.txt` as `ip path status`. Stop after five.
4. Count the lines in the log whose status is `401`. (Check your answer: it is 27.)
5. Count the lines whose size is `-`. (Check your answer: it is 12.)
6. Write `status_of(line)` that returns the status code of a line, or `None` if the line has fewer than 10 parts. Test it with a blank line.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Make a list of all the different paths that gave a `404`. Use a set to remove repeats.
2. Count how many requests came from `203.0.113.45`. What kind of request is most common for that address?
3. Add up the sizes of all the lines that have a size. Skip the `-` lines.

::::::::::::::::::::::::::::::::::::::::::::::::

## Concepts Bridge: Trusting Data from Outside {#week-2-bridge}

**Time: 30 minutes.** Reading 15 minutes, activities 10 minutes, checking the model answer 5 minutes.

### Why this matters

This week your programs read files. A file is **data from outside** your program. So is a download, a web form, or a message from another system. You did not write it, and you cannot be sure about it.

Outside data may be:

- **wrong**: a typo, or a missing column,
- **damaged**: a file cut short, or saved with the wrong encoding,
- **hostile**: written on purpose by someone who wants your program to misbehave.

The safest habit is simple. Do not trust data until your program has checked it. This idea is used every day in cyber security, and it also makes data science work more reliable.

### Data only, or can run code

Some ways of loading data can only ever produce *data*: text, numbers, lists and dictionaries. Other ways can *run code* hidden inside the data. Loading a file should never run anything.

| Way of loading | What it does | Safe for data from outside? |
|---|---|---|
| `json.load`, `json.loads` | Reads JSON and builds dictionaries, lists, strings, numbers | **Data only.** Safe from running code. |
| `csv.reader`, `csv.DictReader` | Reads CSV and gives lists or dictionaries of strings | **Data only.** Safe from running code. |
| `file.read()`, looping over lines | Gives plain text | **Data only.** It is just text. |
| `int()`, `float()` | Turns text into a number, or raises `ValueError` | **Data only.** Fails safely. |
| `eval(text)` | Treats the text as a Python expression and *runs* it | **Can run code.** Do not use on outside text. |
| `pickle.load` | Rebuilds Python objects from a binary file, and can run code while doing so | **Can run code.** Do not use on files you did not make. |

A **data-only** format cannot carry instructions for the computer, only values. That is why JSON and CSV are the right choice for files you share.

### A harmless illustration

Suppose a form gives your program the text `"2 + 3"` and you want a number from it. Compare two ways:

```python
print(eval("2 + 3"))

try:
    print(int("2 + 3"))
except ValueError as error:
    print("ValueError:", error)
```

```output
5
ValueError: invalid literal for int() with base 10: '2 + 3'
```

`eval` did not just read the text. It *ran* it as Python and gave back `5`. If the text had been something else, `eval` would have run that too, and your program cannot tell the difference. The danger is not this sum. The danger is that `eval` runs *whatever* arrives.

`int` only knows how to read a whole number. Anything else is refused with a `ValueError`. It fails safely.

`pickle` is dangerous in the same way. A pickle file is not only values. It can contain steps for rebuilding objects, and those steps can run code. The rule is: never load a pickle file from someone else, or from anywhere you do not control. We do not use `pickle` or `eval` in this course for that reason.

### Validate what you load

Data-only formats cannot run code, but they can still be *wrong*. A JSON record can be perfectly valid and still be nonsense for your program. So after loading, check three things:

| Check | Question | Example |
|---|---|---|
| **Types** | Is each value the kind of thing I expect? | `on_loan` must be `True` or `False`, not `"yes"` |
| **Keys** | Are all the keys I need there? | A book needs `title`, `author` and `isbn` |
| **Ranges** | Is the value sensible? | `attempts` should not be negative |

The rule for this week has two parts:

1. **Prefer data-only formats** (JSON, CSV, plain text) for anything that comes from outside.
2. **Validate what you load.** Check types, keys and ranges before you use the data.

Your `Book.from_dict` in the Build does a small check of this kind.

::::::::::::::::::::::::::::::::::::: challenge

### Activity 1: sort the loading methods (5 minutes)

Sort these into **data only** and **can run code**:

1. `json.loads(text)`
2. `eval(text)`
3. `csv.DictReader(file)`
4. `pickle.load(file)`
5. `int(text)`
6. `for line in file:`

### Activity 2: spot what to check (5 minutes)

Your program loads this record from a file a colleague sent. It is valid JSON. It should describe one user's failed logins.

```output
{"user": "user01", "failed_logins": "many", "locked": "no"}
```

Write down at least three things your code should check before it trusts the record. Think about types, keys and ranges. Which key might be missing?

:::::::::::::::: solution

### Model answer

**Activity 1.**

- Data only: `json.loads`, `csv.DictReader`, `int`, and looping over the lines of a file.
- Can run code: `eval` and `pickle.load`.

**Activity 2.** Good checks:

- **Type:** `failed_logins` should be a whole number, but here it is the text `"many"`. Reject it.
- **Type:** `locked` should be `true` or `false`, but here it is the text `"no"`. A text value `"no"` is not the same as `false`, and in Python a non-empty string counts as true, so a check like `if record["locked"]:` would go wrong.
- **Keys:** check that `user`, `failed_logins` and `locked` are all present. Another record might lack one, and `record["locked"]` would raise `KeyError`.
- **Range:** `failed_logins` should not be negative.

If any check fails, print a clear message and skip the record. Do not let bad data reach the rest of your program.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

### Further reading

- Python Software Foundation (2026) *json — JSON encoder and decoder*. Available at: https://docs.python.org/3/library/json.html (Accessed: 11 November 2026).
- Python Software Foundation (2026) *pickle — Python object serialization* (see the security warning at the top of the page). Available at: https://docs.python.org/3/library/pickle.html (Accessed: 11 November 2026).
- Python Software Foundation (2026) *csv — CSV File Reading and Writing*. Available at: https://docs.python.org/3/library/csv.html (Accessed: 11 November 2026).

## Practice task: Web-Log Converter, and Save and Load for the Library {#week-2-practice}

:::::::::::::::::::::::::::::::::::::::: callout

### Files for this task

The easiest way to get every file is the [course zip file](data/course-data.zip) from the Setup page. Unzip it and open the folder in PyCharm. The programs find the data files by their place in that folder, so keep the folder layout. You can also download single files here:

- [log_converter_starter.py](files/week-2/log_converter_starter.py)
- [solution/log_converter.py](files/week-2/solution/log_converter.py)
- [solution/library.py](files/week-2/solution/library.py)
- [solution/main.py](files/week-2/solution/main.py)
- [test_log_converter.py](files/week-2/test_log_converter.py)
- [test_library.py](files/week-2/test_library.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time guide: 2 hours.** This is your portfolio item for Week 2. Your tutor marks it at the end of the week.

### Goal

You build two things.

- **Part A (about 60 minutes):** a program that reads the web log and writes it out as a CSV file.
- **Part B (about 45 minutes):** you add save and load to your Part 1 library, so the books survive between runs.

The last 15 minutes are for tidying, running the tests and writing a short note.

New words this week:

- **Pure function:** a function that only takes values and returns a value. It does not read files, print or change anything else. It is easy to test.
- **Round trip:** saving something and loading it back, and getting the same thing.
- **Class method:** a method that belongs to the class itself, not to one object. See the box below.

### Files

| File | What it is |
|---|---|
| `log_converter_starter.py` | Part A starter with TODOs. Copy it to your own folder and rename the copy `log_converter.py`. |
| `test_log_converter.py` | Tests for Part A. |
| `test_library.py` | Tests for Part B. |
| `solution/` | Model answers: `log_converter.py`, `library.py`, `main.py`. Try the task yourself first. |

### What you start with

- The log file `assets/files/web_log.txt` in the course folder. It has 200 synthetic lines. Section 2.4 explains the format.
- Your own `library.py` and `main.py` from Part 1 Week 6. If yours is not finished, copy the Part 1 Week 6 model solution instead.

### Part A: the web-log converter

#### Step 1: Set up the folder (5 min)

1. Make a new folder for Week 2, for example `week8_build`, and open it as a project in PyCharm.
2. Copy `log_converter_starter.py` into it and rename the copy `log_converter.py`.
3. The program needs `web_log.txt`. If your folder is **inside the course folder**, the program finds it by itself. If it is somewhere else, copy `assets/files/web_log.txt` into your folder, next to `log_converter.py`.
4. Run `log_converter.py`. It should run without errors and print nothing yet.

#### Step 2: Write `parse_line(line)` (15 min)

The function takes one line of text and returns a dictionary, or `None`.

- Use `line.split()`. If there are **fewer than 10 parts**, return `None`. This covers blank and damaged lines.
- The dictionary keys are `ip`, `date`, `time`, `method`, `path`, `status`, `size`. All the values are **strings**.
- `date` looks like `09/Nov/2026`. `time` looks like `07:13:45`. See "Split the date from the time" in Section 2.4.
- When the log has `-` for the size, use the empty string `""`.

Example:

```output
192.0.2.33 - - [09/Nov/2026:07:13:45 +0800] "GET /contact.html HTTP/1.1" 200 2260
```

gives

```output
{'ip': '192.0.2.33', 'date': '09/Nov/2026', 'time': '07:13:45', 'method': 'GET', 'path': '/contact.html', 'status': '200', 'size': '2260'}
```

Try it in a few lines at the bottom of the file first, then delete those lines.

#### Step 3: Write `read_log(path)` and `write_csv(records, path)` (15 min)

- `read_log` opens the file (mode `"r"`, `encoding="utf-8"`), loops over the lines, and returns a list of the dictionaries. It skips the lines where `parse_line` gives `None`.
- `write_csv` uses `csv.DictWriter` with the `FIELDNAMES` list that is already in the file. Open the file with `"w"`, `newline=""` and `encoding="utf-8"`. Write the header, then all the records.

#### Step 4: Write `count_status(records)` and `main()` (10 min)

- `count_status` returns a dictionary such as `{"200": 143, "404": 16}`. The keys are the status strings.
- In `main()`, after the "cannot find" check that is already there: read the log, write `OUTPUT_FILE`, then print how many lines were converted and the status counts, one per line, in order.

Expected output:

```output
Converted 200 lines to web_log.csv
Status counts:
  200: 143
  304: 12
  401: 27
  404: 16
  500: 2
```

#### Step 5: Test Part A (15 min)

Run the tests (see "Run the tests" below). The most important test checks that your CSV rows are **identical** to the course's own `assets/data/web_log.csv`. If it fails, the failure message shows the first row that differs. Open `web_log.csv` (your output) in PyCharm and compare.

Part A is done when `test_log_converter.py` passes.

### Part B: save and load for the library

#### Step 6: Copy your files, then add `to_dict` and `from_dict` (15 min)

Copy your `library.py` and `main.py` from Part 1 Week 6 into your Week 2 folder. **Do not change the Part 1 interface.** Everything that worked before must still work.

Add these to `Book`:

```python
def to_dict(self):
    ...
```

It returns `{"title": ..., "author": ..., "isbn": ..., "on_loan": ...}`.

```python
@classmethod
def from_dict(cls, data):
    ...
```

It takes a dictionary like the one above and returns a `Book` with `on_loan` set to the saved value.

**What is `@classmethod`?** A normal method works on one object and gets `self`. A class method belongs to the class and gets `cls`, which is the class itself. Here `from_dict` has no book yet, because it is *making* one, so it cannot use `self`. Inside it, `cls(title, author, isbn)` makes a new `Book`. You call it on the class: `Book.from_dict(data)`. Write `@classmethod` on the line above `def`, and use `cls` instead of `self`. That is all you need to know for now.

Hint: `__init__` sets `on_loan` to `False`, so set `book.on_loan` after you make the book.

Check that `from_dict` does a little validation. The model solution raises `ValueError` if `on_loan` is not `True` or `False`, and a missing key gives `KeyError`. See the Concepts Bridge.

#### Step 7: Add `save` and `load` to `Library` (15 min)

```python
def save(self, path):
    ...

@classmethod
def load(cls, path):
    ...
```

- `save` writes a JSON **list** of book dictionaries, with `indent=2` and `encoding="utf-8"`. Use `json.dump` and `to_dict`. Add `import json` at the top.
- `load` reads the file and returns a `Library` with the books added. Use `Book.from_dict` for each one.
- If the file does **not exist**, `load` returns an empty `Library`. Use `try` and `except FileNotFoundError`.
- If the file is not a list, raise `ValueError`.

#### Step 8: Change `main.py` (15 min)

- Put a constant near the top: `LIBRARY_FILE = Path(__file__).parent / "library.json"` (add `from pathlib import Path`). The file is saved next to `main.py`.
- At the start of `main()`, load the library with `Library.load(LIBRARY_FILE)` instead of `Library()`.
- When the user chooses Quit, call `library.save(LIBRARY_FILE)` and print `Goodbye. Books saved.`
- If `library.json` exists but is damaged, `load` raises an error. Catch it in `main()`, print a clear message, and stop *without* saving, so you do not write over the damaged file.

Try it: run `main.py`, add a book, choose Quit. Run it again and list the books. Your book should still be there. Open `library.json` in PyCharm to see how the books are stored.

### Finish: tidy, test and write the note (15 min)

1. Check that each new function and method has a docstring.
2. Run both test files (see below). Fix anything that fails.
3. Write `data_note.txt`: 5 or 6 sentences in your own words. Think about these questions:
   1. Why did you use JSON for the library but CSV for the log?
   2. What could go wrong when your program loads a file that someone else made?
   3. What does your code check before it trusts the data?
   4. Why is it safer to use `json` than `pickle` or `eval`?

### Check your work

- [ ] `log_converter.py` runs and prints the line count and the status counts.
- [ ] `web_log.csv` has a header and 200 rows, and matches the course CSV.
- [ ] `parse_line` returns `None` for a blank line, and `""` for a missing size.
- [ ] `Book.to_dict` and `Book.from_dict` restore `on_loan`.
- [ ] `Library.save` writes JSON and `Library.load` reads it back. A missing file gives an empty library.
- [ ] `main.py` loads at the start and saves on Quit, and prints `Goodbye. Books saved.`
- [ ] The Part 1 menu still works.
- [ ] Every file is opened with `with` and `encoding="utf-8"` (and `newline=""` for CSV).
- [ ] `data_note.txt` has 5 or 6 sentences in your own words.

### Run the tests

From the top folder of the course repository, point `MINI_PROJECT_DIR` at your own folder. It must contain `log_converter.py`, `library.py` and `main.py`.

PowerShell:

```output
$env:MINI_PROJECT_DIR = "C:\path\to\week8_build"
python -m pytest weeks/week-2/practice
```

Mac or Linux:

```output
MINI_PROJECT_DIR=/path/to/week8_build python -m pytest weeks/week-2/practice
```

If pytest is missing, run `python -m pip install pytest`. Without `MINI_PROJECT_DIR`, the tests run against the model solution in `solution/`.

The tests write only into temporary folders. They never change your `library.json`.

### Model solution

Try it yourself first. Then compare with [solution/log_converter.py](files/week-2/solution/log_converter.py), [solution/library.py](files/week-2/solution/library.py) and [solution/main.py](files/week-2/solution/main.py).

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- with closes the file for you, even if something goes wrong.
- The mode "r" reads, "w" replaces and "a" adds to the end.
- Use strip() to remove the newline from each line.
- Use the csv module, not split(","), because values can contain commas.
- Open CSV files with newline="" .
- Everything you read from a CSV file is a string; convert it yourself.
- JSON looks like Python dictionaries and lists.
- json.dump and json.load work with files; dumps and loads work with strings.
- JSON cannot hold your own objects until you turn them into dictionaries.
- A log line holds an address, a time, a request, a status code and a size.
- A 401 means a login failed; a 404 means the page was not found.
- Check that a line has enough parts before you use it.
- Data from outside may be wrong, damaged or hostile.
- JSON and CSV hold data only. pickle and eval() can run code.
- Check what you load before you trust it.
- Read, check and convert data in small functions; keep file handling in main().

::::::::::::::::::::::::::::::::::::::::::::::::
