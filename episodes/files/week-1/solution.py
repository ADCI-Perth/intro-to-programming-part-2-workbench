"""Week 1 practice: a letter-frequency analyser (model solution).

The program reads a passage of text, counts how often each letter from
a to z appears, and prints a table of the ten most common letters with a
bar chart made of # characters.
"""

from pathlib import Path

# Path(__file__) is the location of this file. The line below walks up three
# folders to the course folder, then into assets. Week 2 explains files.
ASSETS = Path(__file__).resolve().parents[3] / "assets"
TEXT_FILE = ASSETS / "files" / "sample_text.txt"

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def read_text(path):
    """Return the whole text file as one string."""
    with open(path, encoding="utf-8") as file:
        return file.read()


def clean(text):
    """Return the text in lower case."""
    return text.lower()


def count_letters(text):
    """Return a dictionary with a count for each of the 26 letters a to z."""
    counts = {}
    for letter in ALPHABET:
        counts[letter] = 0
    for character in clean(text):
        if character in ALPHABET:
            counts[character] = counts[character] + 1
    return counts


def total_letters(counts):
    """Return the total of all the counts."""
    return sum(counts.values())


def percentages(counts):
    """Return a dictionary of letter -> percent of all letters, to 1 decimal place."""
    total = total_letters(counts)
    result = {}
    for letter in counts:
        if total == 0:
            result[letter] = 0.0
        else:
            result[letter] = round(counts[letter] / total * 100, 1)
    return result


def top_letters(counts, n):
    """Return the n most common letters as a list of (letter, count) tuples.

    The biggest count comes first. Letters with the same count are in
    alphabetical order.
    """
    pairs = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    return pairs[:n]


def format_row(letter, count, percent):
    """Return one table row, for example 'e           96    12.3'."""
    return f"{letter:<8}{count:>6}{percent:>8.1f}"


def bar(percent):
    """Return a bar of # characters, one for each whole percent."""
    return "#" * int(percent)


def main():
    text = read_text(TEXT_FILE)
    counts = count_letters(text)
    shares = percentages(counts)

    print("Letter frequency: sample_text.txt")
    print(f"Characters in the file: {len(text):,}")
    print(f"Letters a to z counted: {total_letters(counts):,}")
    print()
    print(f"{'Letter':<8}{'Count':>6}{'%':>8}  Bar")
    print("-" * 36)
    for letter, count in top_letters(counts, 10):
        percent = shares[letter]
        print(format_row(letter, count, percent) + "  " + bar(percent))


if __name__ == "__main__":
    main()
