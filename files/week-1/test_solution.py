"""Tests for the Week 1 practice task.

To test your own work, change the import below from `solution` to `starter`.
"""

import solution as freq


def test_clean_makes_lower_case():
    assert freq.clean("Hello, World!") == "hello, world!"
    assert freq.clean("ABC abc 123") == "abc abc 123"


def test_count_letters_has_all_26_letters():
    counts = freq.count_letters("")
    assert len(counts) == 26
    assert counts["a"] == 0
    assert counts["z"] == 0


def test_count_letters_small_text():
    counts = freq.count_letters("banana")
    assert counts["a"] == 3
    assert counts["n"] == 2
    assert counts["b"] == 1
    assert counts["c"] == 0


def test_count_letters_ignores_case():
    counts = freq.count_letters("Aa AA")
    assert counts["a"] == 4


def test_count_letters_ignores_other_characters():
    counts = freq.count_letters("café 123, ok!")
    assert "é" not in counts
    assert " " not in counts
    assert "1" not in counts
    assert counts["c"] == 1
    assert counts["e"] == 0
    assert freq.total_letters(counts) == 5


def test_total_letters():
    assert freq.total_letters(freq.count_letters("banana")) == 6
    assert freq.total_letters(freq.count_letters("1 2 3 !")) == 0


def test_percentages_small_text():
    shares = freq.percentages(freq.count_letters("aab"))
    assert shares["a"] == 66.7
    assert shares["b"] == 33.3
    assert shares["c"] == 0.0


def test_percentages_no_letters_does_not_crash():
    shares = freq.percentages(freq.count_letters("123"))
    assert len(shares) == 26
    assert shares["a"] == 0.0


def test_top_letters_sorted_by_count():
    counts = freq.count_letters("banana")
    assert freq.top_letters(counts, 3) == [("a", 3), ("n", 2), ("b", 1)]


def test_top_letters_ties_are_alphabetical():
    counts = freq.count_letters("cab bac")
    assert freq.top_letters(counts, 3) == [("a", 2), ("b", 2), ("c", 2)]
    assert len(freq.top_letters(counts, 5)) == 5


def test_format_row():
    assert freq.format_row("e", 96, 12.3) == "e           96    12.3"
    assert freq.format_row("a", 7, 8.0) == "a            7     8.0"
    assert len(freq.format_row("z", 1, 0.1)) == 22


def test_bar():
    assert freq.bar(12.3) == "############"
    assert freq.bar(5.0) == "#####"
    assert freq.bar(0.9) == ""


def test_sample_text_real_numbers():
    text = freq.read_text(freq.TEXT_FILE)
    counts = freq.count_letters(text)
    assert freq.total_letters(counts) == 779
    assert counts["e"] == 96
    assert counts["j"] == 0
    assert freq.percentages(counts)["e"] == 12.3


def test_sample_text_top_five():
    text = freq.read_text(freq.TEXT_FILE)
    counts = freq.count_letters(text)
    assert freq.top_letters(counts, 5) == [
        ("e", 96), ("a", 67), ("s", 64), ("t", 62), ("o", 60),
    ]
