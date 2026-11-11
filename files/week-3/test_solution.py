"""Tests for the Week 3 practice task.

To test your own work, change the import below from `solution` to `starter`.

The last three tests are for the optional stretch (the integrity checker).
They fail until you write `file_hash` and `verify_file`. That is fine.
"""

import hashlib

import solution as checker

# A small made-up list, so the tests do not depend on the real file.
COMMON = {"password", "123456", "qwerty", "sunshine"}


def test_load_common_passwords_from_a_small_file(tmp_path):
    path = tmp_path / "common.txt"
    path.write_text("Password\n\n123456\n  qwerty  \n", encoding="utf-8")
    assert checker.load_common_passwords(path) == {"password", "123456", "qwerty"}


def test_load_common_passwords_reads_the_course_file():
    common = checker.load_common_passwords(checker.COMMON_FILE)
    assert isinstance(common, set)
    assert len(common) == 50
    assert "password" in common
    assert "" not in common


def test_check_length():
    assert checker.check_length("abcdefghijkl") is True        # 12 characters
    assert checker.check_length("abcdefghijk") is False        # 11 characters
    assert checker.check_length("abcdefgh", minimum=8) is True
    assert checker.check_length("", minimum=1) is False


def test_has_upper_and_has_lower():
    assert checker.has_upper("blueKettle") is True
    assert checker.has_upper("bluekettle9!") is False
    assert checker.has_lower("BLUEkETTLE") is True
    assert checker.has_lower("BLUEKETTLE9!") is False


def test_has_digit():
    assert checker.has_digit("kettle7") is True
    assert checker.has_digit("kettle") is False
    assert checker.has_digit("") is False


def test_has_symbol():
    assert checker.has_symbol("kettle!") is True
    assert checker.has_symbol("blue_kettle") is True
    assert checker.has_symbol("kettle7") is False
    assert checker.has_symbol("blue kettle 7") is False        # a space is not a symbol


def test_is_common_ignores_case():
    assert checker.is_common("password", COMMON) is True
    assert checker.is_common("PassWord", COMMON) is True
    assert checker.is_common("Blue-Kettle-47-Rain", COMMON) is False


def test_find_problems_none_for_a_good_password():
    assert checker.find_problems("Blue-Kettle-47-Rain", COMMON) == []


def test_find_problems_lists_every_problem_in_order():
    assert checker.find_problems("sunshine", COMMON) == [
        "It is shorter than 12 characters.",
        "It has no upper-case letter.",
        "It has no digit.",
        "It has no symbol.",
        "It is on the list of common passwords.",
    ]
    assert checker.find_problems("TEAPOT99", COMMON) == [
        "It is shorter than 12 characters.",
        "It has no lower-case letter.",
        "It has no symbol.",
    ]


def test_strength_weak():
    assert checker.strength("qwerty", COMMON) == "weak"        # common and short
    assert checker.strength("SUNSHINE", COMMON) == "weak"      # common, 8 long
    assert checker.strength("Ab1!xyz", COMMON) == "weak"       # 7 characters


def test_strength_fair_and_strong():
    assert checker.strength("Ab1!wxyz", COMMON) == "fair"      # 8 long, under 12
    assert checker.strength("purple teapot morning walk", COMMON) == "fair"
    assert checker.strength("Blue-Kettle-47-Rain", COMMON) == "strong"


# ---------------------------------------------------------------------------
# STRETCH tests (optional). These fail until the stretch is done.
# ---------------------------------------------------------------------------

def test_file_hash_matches_hashlib(tmp_path):
    path = tmp_path / "data.bin"
    path.write_bytes(b"hello")
    digest = checker.file_hash(path)
    assert len(digest) == 64
    assert digest == hashlib.sha256(b"hello").hexdigest()


def test_file_hash_changes_when_one_byte_changes(tmp_path):
    first = tmp_path / "first.txt"
    second = tmp_path / "second.txt"
    first.write_bytes(b"Total: 100\n")
    second.write_bytes(b"Total: 900\n")
    assert checker.file_hash(first) != checker.file_hash(second)


def test_verify_file(tmp_path):
    path = tmp_path / "report.txt"
    path.write_bytes(b"All systems normal.\n")
    good = hashlib.sha256(b"All systems normal.\n").hexdigest()
    assert checker.verify_file(path, good) is True
    assert checker.verify_file(path, "  " + good.upper() + "\n") is True
    assert checker.verify_file(path, "0" * 64) is False
