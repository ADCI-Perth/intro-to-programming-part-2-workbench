"""Section 5.4: find, drop and fill missing values."""

from pathlib import Path

import pandas as pd

# Path(__file__) is this file. parents[4] is the top folder of the course.
# These two lines find the course copy of the web log from any working folder.
ASSETS = Path(__file__).resolve().parents[4] / "assets"
LOG_FILE = ASSETS / "data" / "web_log.csv"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv(LOG_FILE)


print(df.tail(3))
print(df.isna().sum())
print(df["size"].isna().sum())

no_size = df[df["size"].isna()]
print(no_size["status"].value_counts())

print(df["size"].count())
print(df["size"].sum())
print(df["size"].mean())

dropped = df.dropna(subset=["size"])
print(dropped.shape)
print(dropped["size"].mean())

filled = df["size"].fillna(0)
print(filled.tail(3))
print(filled.mean())

df["size_filled"] = df["size"].fillna(0).astype(int)
print(df[["status", "size", "size_filled"]].tail(3))
print(df["size_filled"].sum())
