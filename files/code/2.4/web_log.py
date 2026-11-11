"""Section 2.4: reading a web log line by line. Reads assets/files/web_log.txt."""

from pathlib import Path

# This file is in weeks/week-2/lessons/2.4_code, four folders below the course folder.
ASSETS = Path(__file__).resolve().parents[4] / "assets"
log_file = ASSETS / "files" / "web_log.txt"

# Take one line apart.
line = '192.0.2.33 - - [09/Nov/2026:07:13:45 +0800] "GET /contact.html HTTP/1.1" 200 2260'

parts = line.split()
print(len(parts))
print(parts)

ip = parts[0]
stamp = parts[3].strip("[")
method = parts[5].strip('"')
path = parts[6]
status = parts[8]
size = parts[9]

print(ip)
print(stamp)
print(method)
print(path)
print(status, size)

# Split the date from the time.
pieces = stamp.split(":")
print(pieces)
date = pieces[0]
time = ":".join(pieces[1:])
print(date)
print(time)

# Read the first three lines of the real log.
with open(log_file, "r", encoding="utf-8") as file:
    count = 0
    for line in file:
        parts = line.split()
        print(parts[0], parts[6], parts[8])
        count = count + 1
        if count == 3:
            break

# Count the lines and the "not found" answers in the whole log.
total = 0
not_found = 0
with open(log_file, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.split()
        if len(parts) < 10:
            continue
        total = total + 1
        if parts[8] == "404":
            not_found = not_found + 1

print(total, "lines")
print(not_found, "with status 404")

# A line with no size has "-" in the last place.
with open(log_file, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.split()
        if parts[9] == "-":
            print(line.strip())
            break
