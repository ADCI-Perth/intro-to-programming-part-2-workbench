"""Week 1 practice: a letter-frequency analyser.

The program reads a passage of text, counts how often each letter from
a to z appears, and prints a table of the ten most common letters with a
bar chart made of # characters.

Fill in each TODO. Keep the function names, because the tests look for them.
"""

from pathlib import Path

# ---------------------------------------------------------------------------
# GIVEN: finding and reading the file. Leave this part as it is.
# Week 2 explains how reading files works.
# ---------------------------------------------------------------------------

# Path(__file__) is the location of this file. The line below walks up three
# folders to the course folder, then into assets.
ASSETS = Path(__file__).resolve().parents[3] / "assets"
TEXT_FILE = ASSETS / "files" / "sample_text.txt"

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def read_text(path):
    """Return the whole text file as one string."""
    # Leave this function as it is. encoding="utf-8" tells Python how the
    # bytes in the file turn back into characters (see Section 1.3).
    with open(path, encoding="utf-8") as file:
        return file.read()


# ---------------------------------------------------------------------------
# YOUR JOB: fill in the functions below.
# ---------------------------------------------------------------------------

def clean(text):
    """Return the text in lower case."""
    # TODO: use a string method from Section 1.2.
    pass


def count_letters(text):
    """Return a dictionary with a count for each of the 26 letters a to z.

    Every letter in ALPHABET is a key, even when its count is 0.
    Upper-case letters count as their lower-case letter.
    Everything else (digits, spaces, punctuation, letters such as é) is ignored.
    """
    # TODO: start a dictionary with every letter in ALPHABET set to 0.
    # TODO: loop over clean(text). Add 1 when the character is in ALPHABET.
    pass


def total_letters(counts):
    """Return the total of all the counts."""
    # TODO: add up counts.values().
    pass


def percentages(counts):
    """Return a dictionary of letter -> percent of all letters, to 1 decimal place.

    If the total is 0, every percent is 0.0 (no crash).
    """
    # TODO: percent = count / total * 100, rounded with round(value, 1).
    pass


def top_letters(counts, n):
    """Return the n most common letters as a list of (letter, count) tuples.

    The biggest count comes first. Letters with the same count are in
    alphabetical order.
    """
    # TODO: sort counts.items() (see the hint in the README), then slice [:n].
    pass


def format_row(letter, count, percent):
    """Return one table row, for example 'e           96    12.3'.

    The letter is left-aligned in 8 characters. The count is right-aligned
    in 6 characters. The percent is right-aligned in 8 characters with
    1 decimal place.
    """
    # TODO: one f-string with three format specs.
    pass


def bar(percent):
    """Return a bar of # characters, one for each whole percent.

    For example bar(12.3) is '############' (12 characters) and bar(0.9) is ''.
    """
    # TODO: use int(percent) and the * operator on a string.
    pass


def main():
    # TODO: read the text with read_text(TEXT_FILE).
    # TODO: count the letters and work out the percentages.
    # TODO: print a heading, the number of characters and the number of letters.
    # TODO: print a header row, then one row for each of the top 10 letters,
    #       with its bar at the end of the row.
    pass


# Leave the next two lines as they are. They mean "run main() when this file is
# run directly" (Part 1, Week 6).
if __name__ == "__main__":
    main()
