"""Section 5.3: group rows and work out one answer for each group."""

from pathlib import Path

import pandas as pd

# Path(__file__) is this file. parents[4] is the top folder of the course.
# These two lines find the course copy of the web log from any working folder.
ASSETS = Path(__file__).resolve().parents[4] / "assets"
LOG_FILE = ASSETS / "data" / "web_log.csv"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv(LOG_FILE)


per_ip = df.groupby("ip").size()
print(per_ip.head())
print(per_ip["203.0.113.77"])

busiest = per_ip.sort_values(ascending=False)
print(busiest.head(3))

print(df.groupby("status")["size"].mean())
print(df.groupby("status")["size"].sum())
print(df.groupby("status")["size"].count())
print(df.groupby("status").size())
