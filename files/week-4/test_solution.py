"""Tests for the Week 4 practice task.

To test your own work, change the import below from `solution` to `starter`.
"""

import numpy as np
import pytest

import solution as stats

# A small table you can check by hand: 4 days (rows) and 2 users (columns).
SMALL = np.array([[2, 10],
                  [4, 10],
                  [4, 20],
                  [6, 40]])
SMALL_DATES = ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04"]
SMALL_USERS = ["userA", "userB"]


def test_load_counts_from_a_small_file(tmp_path):
    path = tmp_path / "tiny.csv"
    path.write_text("date,userA,userB\n2026-01-01,2,10\n2026-01-02,4,30\n",
                    encoding="utf-8")
    dates, users, counts = stats.load_counts(path)
    assert dates == ["2026-01-01", "2026-01-02"]
    assert users == ["userA", "userB"]
    assert counts.shape == (2, 2)
    assert counts.tolist() == [[2, 10], [4, 30]]


def test_load_counts_real_file():
    dates, users, counts = stats.load_counts(stats.COUNTS_FILE)
    assert len(dates) == 28
    assert dates[0] == "2026-10-05"
    assert users == ["user01", "user02", "user03", "user04", "user05", "user06"]
    assert counts.shape == (28, 6)
    assert counts[0].tolist() == [4, 8, 1, 6, 5, 6]
    assert counts.sum() == 991


def test_mean_loop():
    assert stats.mean_loop([2, 4, 4, 6]) == 4
    assert stats.mean_loop([5]) == 5
    # approx allows for tiny rounding differences in decimal numbers.
    assert stats.mean_loop([1, 2]) == pytest.approx(1.5)


def test_mean_loop_agrees_with_user_means():
    assert stats.mean_loop(SMALL[:, 1]) == pytest.approx(stats.user_means(SMALL)[1])


def test_user_means():
    means = stats.user_means(SMALL)
    assert means.shape == (2,)
    # allclose means "equal, allowing for tiny rounding differences".
    assert np.allclose(means, [4, 20])


def test_user_stds():
    # userA: the differences from the mean are -2, 0, 0, 2.
    # Their squares are 4, 0, 0, 4. The mean of the squares is 2,
    # so the standard deviation is the square root of 2.
    stds = stats.user_stds(SMALL)
    assert stds[0] == pytest.approx(2 ** 0.5)
    assert stds[1] == pytest.approx(150 ** 0.5)


def test_daily_totals():
    totals = stats.daily_totals(SMALL)
    assert totals.tolist() == [12, 14, 24, 46]


def test_busiest_day():
    assert stats.busiest_day(SMALL_DATES, SMALL) == ("2026-01-04", 46)


def test_z_scores_small():
    z = stats.z_scores(SMALL)
    assert z.shape == (4, 2)
    root2 = 2 ** 0.5
    assert np.allclose(z[:, 0], [-root2, 0, 0, root2])
    # Every column of z-scores has a mean of 0.
    assert np.allclose(z.mean(axis=0), [0, 0])


def test_unusual_small_with_low_threshold():
    # Only the 40 for userB is more than 1.5 standard deviations away.
    found = stats.unusual(SMALL_DATES, SMALL_USERS, SMALL, threshold=1.5)
    assert found == [("2026-01-04", "userB", 40, 1.63)]


def test_unusual_nothing_found():
    assert stats.unusual(SMALL_DATES, SMALL_USERS, SMALL) == []


def test_unusual_real_file_default_threshold():
    dates, users, counts = stats.load_counts(stats.COUNTS_FILE)
    found = stats.unusual(dates, users, counts)
    assert found == [("2026-10-21", "user04", 41, 5.11),
                     ("2026-10-28", "user02", 19, 4.73)]


def test_unusual_real_file_threshold_two():
    dates, users, counts = stats.load_counts(stats.COUNTS_FILE)
    found = stats.unusual(dates, users, counts, threshold=2.0)
    assert len(found) == 5
    assert [item[0] for item in found] == sorted(item[0] for item in found)
    assert ("2026-10-24", "user01", 2, -2.19) in found


def test_busiest_day_real_file():
    dates, users, counts = stats.load_counts(stats.COUNTS_FILE)
    assert stats.busiest_day(dates, counts) == ("2026-10-21", 71)
