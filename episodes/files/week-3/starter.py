"""Week 3 practice: a password strength checker.

Fill in each TODO. Keep the function names, because the tests look for them.

The core functions are pure: they take values and return values.
Only main() uses input() and print().

Safety: this program must never save a password and must never write one to
a file. Test it with made-up passwords only.
"""

import hashlib
from pathlib import Path

# The course's assets folder, found from this file's own location, so the
# program works from any working folder in PyCharm. Leave these lines as
# they are.
ASSETS = Path(__file__).resolve().parents[3] / "assets"
COMMON_FILE = ASSETS / "files" / "common_passwords.txt"

MINIMUM_LENGTH = 12
WEAK_LENGTH = 8

# The fixed wording of each problem. The tests look for these exact strings,
# so use these names instead of typing the sentences again.
TOO_SHORT = "It is shorter than 12 characters."
NO_UPPER = "It has no upper-case letter."
NO_LOWER = "It has no lower-case letter."
NO_DIGIT = "It has no digit."
NO_SYMBOL = "It has no symbol."
IS_COMMON = "It is on the list of common passwords."


def load_common_passwords(path):
    """Return a set of lower-case passwords, one from each line of the file.

    Spaces and the newline at the ends of each line are removed.
    Empty lines are skipped.
    """
    # TODO: open the file with `with open(path, encoding="utf-8") as file:`.
    # TODO: for each line, use strip() and lower(), and add it to a set.
    # TODO: skip lines that are empty after strip().
    pass


def check_length(password, minimum=MINIMUM_LENGTH):
    """Return True if the password has at least `minimum` characters."""
    # TODO: one line, with len().
    pass


def has_upper(password):
    """Return True if at least one character is an upper-case letter."""
    # TODO: use any(...) with isupper().
    pass


def has_lower(password):
    """Return True if at least one character is a lower-case letter."""
    # TODO: use any(...) with islower().
    pass


def has_digit(password):
    """Return True if at least one character is a digit."""
    # TODO: use any(...) with isdigit().
    pass


def has_symbol(password):
    """Return True if at least one character is a symbol.

    A symbol is any character that is not a letter, a digit or a space.
    """
    # TODO: use any(...). A character is a symbol when it is not isalpha(),
    # TODO: not isdigit(), and not equal to " ".
    pass


def is_common(password, common):
    """Return True if the password is in the set `common`, ignoring case."""
    # TODO: make the password lower case, then use `in`.
    pass


def find_problems(password, common):
    """Return a list of problems with the password, in plain English.

    An empty list means no problems were found. The order is always:
    length, upper case, lower case, digit, symbol, common password.
    """
    # TODO: start with an empty list.
    # TODO: call each check above. When a check fails, append the matching
    # TODO: message (TOO_SHORT, NO_UPPER, NO_LOWER, NO_DIGIT, NO_SYMBOL,
    # TODO: IS_COMMON), in that order.
    # TODO: return the list.
    pass


def strength(password, common):
    """Return "weak", "fair" or "strong".

    The rule, checked in this order:
    1. "weak" if the password is a common password, or is shorter than
       8 characters.
    2. "strong" if find_problems returns an empty list.
    3. "fair" for everything else.
    """
    # TODO: follow the three steps in the docstring, in order.
    pass


# ---------------------------------------------------------------------------
# STRETCH (optional): an integrity checker.
# You do not need this part to meet the checklist. The last three tests fail
# until you write it, and that is fine.
# ---------------------------------------------------------------------------

def file_hash(path):
    """Return the SHA-256 hash of a file, as 64 hexadecimal characters.

    The file is opened in binary mode ("rb"), so the hash is made from the
    exact bytes on the disk.
    """
    # TODO (stretch): open the file with open(path, "rb") and read() it.
    # TODO (stretch): return hashlib.sha256(data).hexdigest().
    pass


def verify_file(path, expected_hash):
    """Return True if the file's SHA-256 hash matches `expected_hash`.

    Upper and lower case in `expected_hash` do not matter, and spaces
    around it are ignored.
    """
    # TODO (stretch): compare file_hash(path) with expected_hash, after
    # TODO (stretch): strip() and lower() on expected_hash.
    pass


def main():
    # TODO: load the common passwords from COMMON_FILE.
    # TODO: remind the user to type made-up passwords only.
    # TODO: ask for a password with input() until an empty line.
    # TODO: for each one, print the rating and each problem on its own line.
    # TODO: do not save the password anywhere.
    pass


# Leave the next two lines as they are. They mean "run main() when this file is
# run directly" (Part 1, Week 6).
if __name__ == "__main__":
    main()
