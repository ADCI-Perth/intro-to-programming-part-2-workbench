"""Section 5.2: filter rows with boolean masks."""

from pathlib import Path

import pandas as pd

# Path(__file__) is this file. parents[4] is the top folder of the course.
# These two lines find the course copy of the web log from any working folder.
ASSETS = Path(__file__).resolve().parents[4] / "assets"
LOG_FILE = ASSETS / "data" / "web_log.csv"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

df = pd.read_csv(LOG_FILE)


mask = df["status"] == 404
print(mask.head())
print(mask.sum())

not_found = df[mask]
print(not_found.head())
print(len(not_found))

failed = df[(df["path"] == "/login") & (df["status"] == 401)]
print(len(failed))
print(failed.head(3))

problems = df[(df["status"] == 401) | (df["status"] == 404)]
print(len(problems))

same_problems = df[df["status"].isin([401, 404])]
print(len(same_problems))

big_ok = df[(df["status"] == 200) & (df["size"] > 10000)]
print(len(big_ok))
