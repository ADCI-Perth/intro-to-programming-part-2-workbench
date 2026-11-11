"""Section 6.2: a histogram of response sizes, with two different bin counts."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent
ASSETS = Path(__file__).resolve().parents[4] / "assets"

df = pd.read_csv(ASSETS / "data" / "web_log.csv")
sizes = df["size"].dropna()          # 12 rows have no size
print("Sizes with a value:", len(sizes))
print("Smallest:", sizes.min(), "Largest:", sizes.max())

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
ax1.hist(sizes, bins=5)
ax1.set_title("5 bins")
ax1.set_xlabel("Response size (bytes)")
ax1.set_ylabel("Requests (count)")
ax2.hist(sizes, bins=20)
ax2.set_title("20 bins")
ax2.set_xlabel("Response size (bytes)")
ax2.set_ylabel("Requests (count)")
fig.tight_layout()
fig.savefig(HERE / "size_histograms.png", dpi=150)
plt.close(fig)
print("Saved size_histograms.png")
