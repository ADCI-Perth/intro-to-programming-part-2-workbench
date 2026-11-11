"""Section 5.2: string methods on a column, and an hour column."""

from pathlib import Path

import pandas as pd

# Path(__file__) is this file. parents[4] is the top folder of the course.
# These two lines find the course copy of the web log from any working folder.
ASSETS = Path(__file__).resolve().parents[4] / "assets"
LOG_FILE = ASSETS / "data" / "web_log.csv"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv(LOG_FILE)


print(df["time"].head(3))
print(df["time"].str[:2].head(3))

df["hour"] = df["time"].str[:2].astype(int)
print(df[["time", "hour"]].head(3))
print(df["hour"].dtype)

night = df[df["hour"] < 6]
print(len(night))
print(night["ip"].value_counts())

pages = df[df["path"].str.endswith(".html")]
print(len(pages))
print(df["method"].str.lower().head(2))
