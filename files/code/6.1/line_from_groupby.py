"""Section 6.1: plot a Pandas Series made by groupby (requests per hour)."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent
ASSETS = Path(__file__).resolve().parents[4] / "assets"

df = pd.read_csv(ASSETS / "data" / "web_log.csv")
df["hour"] = df["time"].str[:2].astype(int)

per_hour = df.groupby("hour").size()
print(per_hour.head())

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(per_hour.index, per_hour.values, marker="o")
ax.set_title("Web requests per hour of the day")
ax.set_xlabel("Hour of the day (24-hour clock)")
ax.set_ylabel("Requests (count)")
ax.set_ylim(bottom=0)
fig.tight_layout()
fig.savefig(HERE / "requests_per_hour.png", dpi=150)
plt.close(fig)
print("Saved requests_per_hour.png")
