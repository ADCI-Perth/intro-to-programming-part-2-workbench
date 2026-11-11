"""Section 5.3: several answers at once, and tidy results."""

from pathlib import Path

import pandas as pd

# Path(__file__) is this file. parents[4] is the top folder of the course.
# These two lines find the course copy of the web log from any working folder.
ASSETS = Path(__file__).resolve().parents[4] / "assets"
LOG_FILE = ASSETS / "data" / "web_log.csv"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv(LOG_FILE)


summary = df.groupby("status")["size"].agg(["count", "mean", "max"])
print(summary)

per_ip = df.groupby("ip").size()
print(per_ip[per_ip >= 20])

table = per_ip.reset_index(name="requests")
print(table.head(3))

top = table.sort_values(["requests", "ip"], ascending=[False, True])
print(top.head(4))

failed = df[(df["path"] == "/login") & (df["status"] == 401)]
print(failed.groupby("ip").size().sort_values(ascending=False))
