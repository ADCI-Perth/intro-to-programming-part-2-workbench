"""Section 5.1: select columns and make new ones."""

from pathlib import Path

import pandas as pd

# Path(__file__) is this file. parents[4] is the top folder of the course.
# These two lines find the course copy of the web log from any working folder.
ASSETS = Path(__file__).resolve().parents[4] / "assets"
LOG_FILE = ASSETS / "data" / "web_log.csv"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv(LOG_FILE)


status = df["status"]
print(status.head())
print(status.max())
print(df["ip"].nunique())

small = df[["ip", "status"]]
print(small.head())

df["size_kb"] = df["size"] / 1024
df["is_error"] = df["status"] >= 400
print(df[["path", "status", "size", "size_kb", "is_error"]].head())
print(df["is_error"].sum())
