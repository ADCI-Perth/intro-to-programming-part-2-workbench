"""Week 4 practice: login statistics with a z-score check.

The program reads a small table of daily login counts, works out some
statistics with NumPy, and flags counts that are unusual for that user.

Fill in each TODO. Keep the function names, because the tests look for them.
Before you start, install numpy and pytest in the virtual environment of
your project (see the README).
"""

import csv
from pathlib import Path

import numpy as np

# Path(__file__) is this file. parents[3] is the course folder, three levels up.
# If your copy of the data file is somewhere else, change COUNTS_FILE to match.
ASSETS = Path(__file__).resolve().parents[3] / "assets"
COUNTS_FILE = ASSETS / "data" / "login_counts.csv"


def load_counts(path):
    """Read the CSV file and return (dates, users, counts).

    dates is a list of date strings, one per row.
    users is a list of the user names from the header row.
    counts is a 2-D NumPy array of whole numbers: one row per date,
    one column per user.
    """
    # TODO: open the file and make a csv.reader (Week 2).
    # TODO: the first row is the header. The user names are header[1:].
    # TODO: for every other row, add row[0] to dates, and add a list of
    #       int values (from row[1:]) to a list of rows.
    # TODO: turn the list of rows into an array with np.array(...).
    # TODO: return dates, users, counts
    pass


def mean_loop(values):
    """Return the mean of a 1-D sequence of numbers, using a plain for loop."""
    # TODO: add up the values with a for loop, and count them as you go.
    # TODO: return the total divided by how many there are.
    #       Do not use sum(), np.mean() or .mean() here. The loop is the point.
    pass


def user_means(counts):
    """Return a 1-D array holding the mean of each column (each user)."""
    # TODO: one line, with axis=0.
    pass


def user_stds(counts):
    """Return a 1-D array holding the standard deviation of each column."""
    # TODO: one line, with axis=0.
    pass


def daily_totals(counts):
    """Return a 1-D array holding the total of each row (each day)."""
    # TODO: one line, with axis=1.
    pass


def busiest_day(dates, counts):
    """Return (date, total) for the day with the most logins in total."""
    # TODO: get the daily totals, then use argmax() to find the position.
    # TODO: return the date at that position and int(total at that position).
    pass


def z_scores(counts):
    """Return a 2-D array of z-scores, the same shape as counts.

    Each cell is compared with the mean and standard deviation of its own
    column, so each user is compared only with their own usual pattern.
    """
    # TODO: (counts - the column means) / the column standard deviations.
    pass


def unusual(dates, users, counts, threshold=3.0):
    """Return a list of (date, user, count, z) tuples where abs(z) > threshold.

    z is rounded to 2 decimal places. The list is sorted by date.
    """
    # TODO: get the z-scores.
    # TODO: visit every row and column position. When abs(z) is above the
    #       threshold, append (date, user, int(count), round(float(z), 2)).
    # TODO: sort the list and return it.
    pass


def main():
    # TODO: load the file with load_counts(COUNTS_FILE).
    # TODO: print a table with one line per user: name, mean, standard
    #       deviation. Line the columns up with f-string formatting (Week 1).
    # TODO: print the mean for one user from mean_loop and from user_means,
    #       to show that they agree.
    # TODO: print the busiest day and its total.
    # TODO: print each unusual value: date, user, count and z-score.
    pass


# Leave the next two lines as they are.
if __name__ == "__main__":
    main()
