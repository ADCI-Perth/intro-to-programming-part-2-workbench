# Makes the ADCI header logos and favicons for the varnish theme fork from adci-logo-source.jpg.
# Usage (needs Pillow): python make_logo.py adci-logo-source.jpg .
import sys, base64, io
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGBA")
# white background -> transparent (soft edge)
px = im.load()
w, h = im.size
for y in range(h):
    for x in range(w):
        r, g, b, a = px[x, y]
        m = min(r, g, b)
        if m > 235:
            px[x, y] = (r, g, b, 0)
        elif m > 200 and max(r,g,b) - m < 25:
            px[x, y] = (r, g, b, int(255 * (235 - m) / 35))
bbox = im.getbbox(); print("bbox", bbox)
full = im.crop(bbox)
# shield = columns up to the first fully empty gap after the shield
cols = [any(full.getpixel((x, y))[3] > 0 for y in range(full.height)) for x in range(full.width)]
gap = next(x for x in range(20, full.width) if not cols[x])
shield = full.crop((0, 0, gap, full.height)); shield = shield.crop(shield.getbbox())
print("full", full.size, "shield", shield.size)
def svg(img, name):
    buf = io.BytesIO(); img.quantize(64, method=Image.Quantize.FASTOCTREE).save(buf, "PNG", optimize=True)
    b = base64.b64encode(buf.getvalue()).decode()
    W, H = img.size
    open(f"{out}/{name}", "w").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Australian Data and Cyber Institute">'
        f'<image width="{W}" height="{H}" href="data:image/png;base64,{b}" xlink:href="data:image/png;base64,{b}"/></svg>')
    img.save(f"{out}/{name[:-4]}.png")
fit = lambda i, H: i.resize((round(i.width*H/i.height), H), Image.LANCZOS)
svg(fit(full, 160), "adci-logo.svg"); svg(fit(shield, 128), "adci-logo-sm.svg")
# favicons from the shield, on a square transparent canvas
s = max(shield.size); sq = Image.new("RGBA", (s, s), (0,0,0,0)); sq.paste(shield, ((s-shield.width)//2, (s-shield.height)//2))
import os; os.makedirs(f"{out}/favicons/adci", exist_ok=True)
for n, z in [("favicon-16x16.png",16),("favicon-32x32.png",32),("apple-touch-icon.png",180),("android-chrome-192x192.png",192),("android-chrome-512x512.png",512),("mstile-150x150.png",150)]:
    sq.resize((z, z), Image.LANCZOS).save(f"{out}/favicons/adci/{n}")
