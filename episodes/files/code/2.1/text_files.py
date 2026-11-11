"""Section 2.1: text files. Writes notes.txt next to this file, then reads it."""

from pathlib import Path

HERE = Path(__file__).parent
notes_file = HERE / "notes.txt"

# Write a new file. Mode "w" creates the file, or empties it if it exists.
with open(notes_file, "w", encoding="utf-8") as file:
    file.write("Checked the backup at 9 am.\n")
    file.write("Two failed logins from 203.0.113.45.\n")

# Read the whole file into one string.
with open(notes_file, "r", encoding="utf-8") as file:
    text = file.read()

print(text)
print(len(text), "characters")

# Read line by line. Each line still has its newline at the end.
with open(notes_file, "r", encoding="utf-8") as file:
    for line in file:
        print(repr(line))

# strip() removes the newline.
with open(notes_file, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Mode "a" adds to the end and keeps what is there.
with open(notes_file, "a", encoding="utf-8") as file:
    file.write("Rang the café about the router.\n")

# Count the lines, and collect them in a list.
lines = []
with open(notes_file, "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.strip())

print(len(lines), "lines")
print(lines[-1])

# A file that is not there raises FileNotFoundError.
missing_file = HERE / "no_such_file.txt"
try:
    with open(missing_file, "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Cannot find", missing_file.name)

# Paths: the folder this script is in, and a file in it.
print(HERE.name)
print(notes_file.name)
print(notes_file.exists())
