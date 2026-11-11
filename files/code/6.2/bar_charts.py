"""Section 6.2: bar and horizontal bar charts from web_log.csv."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent
ASSETS = Path(__file__).resolve().parents[4] / "assets"

df = pd.read_csv(ASSETS / "data" / "web_log.csv")

# Vertical bars: compare a few short categories.
by_status = df.groupby("status").size()
print(by_status)

fig, ax = plt.subplots()
ax.bar(by_status.index.astype(str), by_status.values)
ax.set_title("Web requests by status code")
ax.set_xlabel("Status code")
ax.set_ylabel("Requests (count)")
fig.tight_layout()
fig.savefig(HERE / "status_bars.png", dpi=150)
plt.close(fig)

# Horizontal bars: long labels, sorted so the biggest is at the top.
top_paths = df.groupby("path").size().sort_values(ascending=False).head(5)
print(top_paths)
top_paths = top_paths.sort_values()      # barh draws the first item at the bottom

fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(top_paths.index, top_paths.values)
ax.set_title("Five most requested pages")
ax.set_xlabel("Requests (count)")
ax.set_ylabel("Page")
fig.tight_layout()
fig.savefig(HERE / "top_pages.png", dpi=150)
plt.close(fig)
print("Saved status_bars.png and top_pages.png")
