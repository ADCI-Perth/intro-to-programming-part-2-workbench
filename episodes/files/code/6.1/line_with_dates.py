"""Section 6.1: two lines on one chart, with a legend and tilted dates."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent
ASSETS = Path(__file__).resolve().parents[4] / "assets"

df = pd.read_csv(ASSETS / "data" / "login_counts.csv")
print(df[["date", "user01", "user04"]].head(3))

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["date"], df["user01"], label="user01")
ax.plot(df["date"], df["user04"], label="user04")
ax.set_title("Daily logins for two users")
ax.set_xlabel("Date")
ax.set_ylabel("Logins (count)")
ax.legend()
ax.set_xticks(df["date"][::3])      # show every third date only
fig.autofmt_xdate()                 # tilt the date labels
fig.tight_layout()
fig.savefig(HERE / "two_users.png", dpi=150)
plt.close(fig)
print("Saved two_users.png")
