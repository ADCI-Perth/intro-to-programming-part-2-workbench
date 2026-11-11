"""Section 2.2: CSV files. Writes logins.csv and summary.csv next to this file."""

import csv
from pathlib import Path

HERE = Path(__file__).parent
logins_file = HERE / "logins.csv"
summary_file = HERE / "summary.csv"

# Write rows with csv.writer. Each row is a list.
rows = [
    ["user01", "Perth, WA", 14],
    ["user02", "Fremantle, WA", 3],
    ["user03", "Joondalup, WA", 27],
]

with open(logins_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["user", "office", "logins"])
    writer.writerows(rows)

# Look at the raw text. The csv module put quotes around values with a comma.
with open(logins_file, "r", encoding="utf-8") as file:
    print(file.read())

# Read with csv.reader. Each row comes back as a list of strings.
with open(logins_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Why not split(",")? It breaks the office into two pieces.
line = 'user01,"Perth, WA",14'
print(line.split(","))

# Read with csv.DictReader. Each row comes back as a dictionary.
total = 0
with open(logins_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["user"], row["logins"])
        total = total + int(row["logins"])

print("Total logins:", total)

# Everything read from a CSV file is a string.
with open(logins_file, "r", newline="", encoding="utf-8") as file:
    records = list(csv.DictReader(file))

print(records[0])
print(records[0]["logins"] + records[1]["logins"])
print(int(records[0]["logins"]) + int(records[1]["logins"]))

# Write dictionaries with csv.DictWriter.
busy = []
for record in records:
    if int(record["logins"]) >= 10:
        busy.append({"user": record["user"], "logins": record["logins"]})

with open(summary_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["user", "logins"])
    writer.writeheader()
    writer.writerows(busy)

with open(summary_file, "r", encoding="utf-8") as file:
    print(file.read())
