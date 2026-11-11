"""Web-log converter: Week 2 starter (Part A).

Copy this file into your own Week 2 folder and rename the copy
log_converter.py. Then fill in each TODO.

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

    This function is given. Leave it as it is.
    It looks next to this file first. Then it looks for
    assets/files/web_log.txt in each folder above this one, which finds
    the file when you work inside the course folder.
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

    A good line has at least 10 parts when split on spaces.
    The dictionary has the keys ip, date, time, method, path, status, size.
    Every value is a string. size is "" when the log shows "-".

    Example line:
    192.0.2.33 - - [09/Nov/2026:07:13:45 +0800] "GET /contact.html HTTP/1.1" 200 2260
    gives:
    {"ip": "192.0.2.33", "date": "09/Nov/2026", "time": "07:13:45",
     "method": "GET", "path": "/contact.html", "status": "200", "size": "2260"}
    """
    # TODO: split the line, check there are at least 10 parts,
    #       then build and return the dictionary.
    pass


def read_log(path):
    """Read a log file and return a list of dictionaries, one per good line.

    Lines where parse_line gives None are skipped.
    """
    # TODO: open the file with "r" and encoding="utf-8", loop over the
    #       lines, and collect the dictionaries from parse_line.
    pass


def write_csv(records, path):
    """Write the records to a CSV file with a header row.

    Use csv.DictWriter with FIELDNAMES. Open the file with "w",
    newline="" and encoding="utf-8".
    """
    # TODO: write the header, then all the records.
    pass


def count_status(records):
    """Return a dictionary of status code -> how many records have it.

    Example: {"200": 2, "404": 1}
    """
    # TODO: count the "status" value of each record.
    pass


def main():
    """Convert web_log.txt to web_log.csv and print a short summary."""
    log_file = find_log_file()
    if log_file is None:
        print("Cannot find web_log.txt.")
        print("Copy assets/files/web_log.txt into the same folder as this file.")
        return
    # TODO: read the log, write OUTPUT_FILE, then print how many lines
    #       were converted and the status counts (see the README).
    pass


if __name__ == "__main__":
    main()
