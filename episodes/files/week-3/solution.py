"""Week 3 practice: a password strength checker (model solution).

The core functions are pure: they take values and return values.
Only main() uses input() and print().

Safety: this program never saves a password and never writes one to a file.
Test it with made-up passwords only.
"""

import hashlib
from pathlib import Path

# The course's assets folder, found from this file's own location, so the
# program works from any working folder in PyCharm.
ASSETS = Path(__file__).resolve().parents[3] / "assets"
COMMON_FILE = ASSETS / "files" / "common_passwords.txt"

MINIMUM_LENGTH = 12
WEAK_LENGTH = 8

# The fixed wording of each problem. The tests look for these exact strings.
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
    common = set()
    with open(path, encoding="utf-8") as file:
        for line in file:
            word = line.strip().lower()
            if word != "":
                common.add(word)
    return common


def check_length(password, minimum=MINIMUM_LENGTH):
    """Return True if the password has at least `minimum` characters."""
    return len(password) >= minimum


def has_upper(password):
    """Return True if at least one character is an upper-case letter."""
    return any(ch.isupper() for ch in password)


def has_lower(password):
    """Return True if at least one character is a lower-case letter."""
    return any(ch.islower() for ch in password)


def has_digit(password):
    """Return True if at least one character is a digit."""
    return any(ch.isdigit() for ch in password)


def has_symbol(password):
    """Return True if at least one character is a symbol.

    A symbol is any character that is not a letter, a digit or a space.
    """
    return any(
        not ch.isalpha() and not ch.isdigit() and ch != " "
        for ch in password
    )


def is_common(password, common):
    """Return True if the password is in the set `common`, ignoring case."""
    return password.lower() in common


def find_problems(password, common):
    """Return a list of problems with the password, in plain English.

    An empty list means no problems were found. The order is always:
    length, upper case, lower case, digit, symbol, common password.
    """
    problems = []
    if not check_length(password):
        problems.append(TOO_SHORT)
    if not has_upper(password):
        problems.append(NO_UPPER)
    if not has_lower(password):
        problems.append(NO_LOWER)
    if not has_digit(password):
        problems.append(NO_DIGIT)
    if not has_symbol(password):
        problems.append(NO_SYMBOL)
    if is_common(password, common):
        problems.append(IS_COMMON)
    return problems


def strength(password, common):
    """Return "weak", "fair" or "strong".

    The rule, checked in this order:
    1. "weak" if the password is a common password, or is shorter than
       8 characters.
    2. "strong" if find_problems returns an empty list.
    3. "fair" for everything else.
    """
    if is_common(password, common) or len(password) < WEAK_LENGTH:
        return "weak"
    if find_problems(password, common) == []:
        return "strong"
    return "fair"


# ---------------------------------------------------------------------------
# STRETCH (optional): an integrity checker.
# ---------------------------------------------------------------------------

def file_hash(path):
    """Return the SHA-256 hash of a file, as 64 hexadecimal characters.

    The file is opened in binary mode ("rb"), so the hash is made from the
    exact bytes on the disk.
    """
    with open(path, "rb") as file:
        data = file.read()
    return hashlib.sha256(data).hexdigest()


def verify_file(path, expected_hash):
    """Return True if the file's SHA-256 hash matches `expected_hash`.

    Upper and lower case in `expected_hash` do not matter, and spaces
    around it are ignored.
    """
    return file_hash(path) == expected_hash.strip().lower()


def main():
    common = load_common_passwords(COMMON_FILE)
    print("Password strength checker.")
    print("Use made-up passwords only. Never type a real password here.")
    print("Press Enter on an empty line to finish.")
    password = input("Password to check: ")
    while password != "":
        print("  Rating:", strength(password, common))
        problems = find_problems(password, common)
        if problems == []:
            print("  No problems found.")
        for problem in problems:
            print("  -", problem)
        password = input("Password to check: ")
    print("Goodbye.")


# Leave the next two lines as they are. They mean "run main() when this file is
# run directly" (Part 1, Week 6).
if __name__ == "__main__":
    main()
