"""Section 5.1: read the web log and take a first look."""

from pathlib import Path

import pandas as pd

# Path(__file__) is this file. parents[4] is the top folder of the course.
# These two lines find the course copy of the web log from any working folder.
ASSETS = Path(__file__).resolve().parents[4] / "assets"
LOG_FILE = ASSETS / "data" / "web_log.csv"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv(LOG_FILE)


print(df.head())
print(df.tail(3))
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()
print(df.describe())
