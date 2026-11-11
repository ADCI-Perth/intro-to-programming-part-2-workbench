"""Web-log converter: Week 2 model solution (Part A).

Reads a web-server log (plain text, one request per line) and writes the
same records as a CSV file with a header row.
"""

import csv
from pathlib import Path

FIELDNAMES = ["ip", "date", "time", "method", "path", "status", "size"]

# The CSV file is written next to this file, in your own folder.
OUTPUT_FILE = Path(__file__).parent / "web_log.csv"


def find_log_file():
    """Return the path of web_log.txt, or None if it cannot be found.

    Looks next to this file first. Then looks for assets/files/web_log.txt
    in each folder above this one, which finds it inside the course folder.
    """
    here = Path(__file__).resolve().parent
    if (here / "web_log.txt").exists():
        return here / "web_log.txt"
    for folder in here.parents:
        candidate = folder / "assets" / "files" / "web_log.txt"
        if candidate.exists():
            return candidate
    return None


def parse_line(line):
    """Turn one log line into a dictionary. Return None for a bad line.

    A good line has at least 10 parts when split on spaces. Every value in
    the dictionary is a string. size is "" when the log shows "-".
    """
    parts = line.split()
    if len(parts) < 10:
        return None
    stamp = parts[3].strip("[")          # 09/Nov/2026:07:13:45
    pieces = stamp.split(":")            # ['09/Nov/2026', '07', '13', '45']
    size = parts[9]
    if size == "-":
        size = ""
    return {
        "ip": parts[0],
        "date": pieces[0],
        "time": ":".join(pieces[1:]),
        "method": parts[5].strip('"'),
        "path": parts[6],
        "status": parts[8],
        "size": size,
    }


def read_log(path):
    """Read a log file and return a list of dictionaries, one per good line."""
    records = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            record = parse_line(line)
            if record is not None:
                records.append(record)
    return records


def write_csv(records, path):
    """Write the records to a CSV file with a header row."""
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(records)


def count_status(records):
    """Return a dictionary of status code -> how many records have it."""
    counts = {}
    for record in records:
        status = record["status"]
        counts[status] = counts.get(status, 0) + 1
    return counts


def main():
    """Convert web_log.txt to web_log.csv and print a short summary."""
    log_file = find_log_file()
    if log_file is None:
        print("Cannot find web_log.txt.")
        print("Copy assets/files/web_log.txt into the same folder as this file.")
        return
    records = read_log(log_file)
    write_csv(records, OUTPUT_FILE)
    print(f"Converted {len(records)} lines to {OUTPUT_FILE.name}")
    print("Status counts:")
    counts = count_status(records)
    for status in sorted(counts):
        print(f"  {status}: {counts[status]}")


if __name__ == "__main__":
    main()
