"""Section 5.2: sort rows and count values."""

from pathlib import Path

import pandas as pd

# Path(__file__) is this file. parents[4] is the top folder of the course.
# These two lines find the course copy of the web log from any working folder.
ASSETS = Path(__file__).resolve().parents[4] / "assets"
LOG_FILE = ASSETS / "data" / "web_log.csv"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv(LOG_FILE)


by_size = df.sort_values("size")
print(by_size[["path", "status", "size"]].head(3))

biggest = df.sort_values("size", ascending=False)
print(biggest[["path", "status", "size"]].head(3))

ordered = df.sort_values(["status", "ip"], ascending=[False, True])
print(ordered[["ip", "time", "path", "status"]].head(5))

print(df["status"].value_counts())
print(df["method"].value_counts())
print(df["ip"].value_counts().head(3))
