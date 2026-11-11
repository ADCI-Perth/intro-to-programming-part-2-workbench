"""Section 3.1: checking input before you use it."""

# An allow-list: the only characters a username may contain.
ALLOWED = set("abcdefghijklmnopqrstuvwxyz0123456789_")

# A set of symbols, used by has_symbol.
SYMBOLS = set("!@#$%&*?")


def is_valid_age(text):
    """Return True if text is a whole number from 0 to 120."""
    try:
        age = int(text)
    except ValueError:
        return False
    return 0 <= age <= 120


def is_valid_postcode(text):
    """Return True if text is exactly four digits, such as "6000"."""
    return len(text) == 4 and text.isdigit()


def has_symbol(text):
    """Return True if at least one character is in SYMBOLS."""
    return any(ch in SYMBOLS for ch in text)


def check_username(name):
    """Return a list of problems with a username. Empty means it is fine."""
    problems = []
    if name.strip() == "":
        problems.append("The username is empty.")
        return problems
    if len(name) < 3:
        problems.append("The username is shorter than 3 characters.")
    if len(name) > 15:
        problems.append("The username is longer than 15 characters.")
    if not all(ch in ALLOWED for ch in name):
        problems.append("Use only lower-case letters, digits and underscores.")
    if name[0].isdigit():
        problems.append("The username must not start with a digit.")
    return problems


print("--- any and all ---")
print(any([False, True, False]))
print(all([True, True, False]))
print(any(ch.isdigit() for ch in "kettle7"))
print(all(ch.isdigit() for ch in "60o0"))

print("--- age ---")
for text in ["34", "abc", "-5", "150", " 61 "]:
    print(repr(text), is_valid_age(text))

print("--- postcode ---")
for text in ["6000", "0800", "600", "60000", "6OOO"]:
    print(repr(text), is_valid_postcode(text))

print("--- symbols ---")
print(has_symbol("kettle!"))
print(has_symbol("kettle"))

print("--- username ---")
for name in ["olivia_t", "", "jw", "9 Lives!", "user01"]:
    print(repr(name), check_username(name))
