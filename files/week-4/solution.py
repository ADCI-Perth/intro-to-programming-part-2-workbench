"""Week 4 practice: login statistics with a z-score check (model solution).

The program reads a small table of daily login counts, works out some
statistics with NumPy, and flags counts that are unusual for that user.
"""

import csv
from pathlib import Path

import numpy as np

# Path(__file__) is this file. parents[3] is the course folder, three levels up.
ASSETS = Path(__file__).resolve().parents[3] / "assets"
COUNTS_FILE = ASSETS / "data" / "login_counts.csv"


def load_counts(path):
    """Read the CSV file and return (dates, users, counts).

    dates is a list of date strings, one per row.
    users is a list of the user names from the header row.
    counts is a 2-D NumPy array of whole numbers: one row per date,
    one column per user.
    """
    dates = []
    rows = []
    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        users = header[1:]
        for row in reader:
            dates.append(row[0])
            rows.append([int(cell) for cell in row[1:]])
    counts = np.array(rows)
    return dates, users, counts


def mean_loop(values):
    """Return the mean of a 1-D sequence of numbers, using a plain for loop."""
    total = 0
    how_many = 0
    for value in values:
        total = total + value
        how_many = how_many + 1
    return total / how_many


def user_means(counts):
    """Return a 1-D array holding the mean of each column (each user)."""
    return counts.mean(axis=0)


def user_stds(counts):
    """Return a 1-D array holding the standard deviation of each column."""
    return counts.std(axis=0)


def daily_totals(counts):
    """Return a 1-D array holding the total of each row (each day)."""
    return counts.sum(axis=1)


def busiest_day(dates, counts):
    """Return (date, total) for the day with the most logins in total."""
    totals = daily_totals(counts)
    position = totals.argmax()
    return dates[position], int(totals[position])


def z_scores(counts):
    """Return a 2-D array of z-scores, the same shape as counts.

    Each cell is compared with the mean and standard deviation of its own
    column, so each user is compared only with their own usual pattern.
    """
    return (counts - user_means(counts)) / user_stds(counts)


def unusual(dates, users, counts, threshold=3.0):
    """Return a list of (date, user, count, z) tuples where abs(z) > threshold.

    z is rounded to 2 decimal places. The list is sorted by date.
    """
    z = z_scores(counts)
    found = []
    for row in range(len(dates)):
        for col in range(len(users)):
            if abs(z[row, col]) > threshold:
                found.append((dates[row], users[col], int(counts[row, col]),
                              round(float(z[row, col]), 2)))
    found.sort()
    return found


def main():
    dates, users, counts = load_counts(COUNTS_FILE)
    print(f"Loaded {counts.shape[0]} days for {counts.shape[1]} users.")
    print()

    means = user_means(counts)
    stds = user_stds(counts)
    print(f"{'User':<8}{'Mean':>8}{'Std dev':>10}")
    for position in range(len(users)):
        print(f"{users[position]:<8}{means[position]:>8.2f}{stds[position]:>10.2f}")
    print()

    # The LO 4 comparison: the loop and the array method give the same answer.
    print(f"Mean for {users[0]} with a loop: {mean_loop(counts[:, 0]):.2f}")
    print(f"Mean for {users[0]} with NumPy:  {means[0]:.2f}")
    print()

    date, total = busiest_day(dates, counts)
    print(f"Busiest day: {date} with {total} logins in total.")
    print()

    print("Unusual values (z-score above 3 or below -3):")
    flagged = unusual(dates, users, counts)
    if len(flagged) == 0:
        print("  None found.")
    for date, user, count, z in flagged:
        print(f"  {date}  {user}  {count:>3} logins  z = {z:.2f}")
    print("Unusual is not the same as wrong. Each one needs a closer look.")


if __name__ == "__main__":
    main()
