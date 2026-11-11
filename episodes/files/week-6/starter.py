"""Week 6 capstone: two charts and a written finding.

Choose ONE option and complete its functions. Leave the other option's
functions as they are (their tests will fail in your copy, and that is fine).

Option A (security): login_attempts.csv, columns date,hour,user,ip,result
Option B (data):     sales.csv, columns date,region,product,units,unit_price

Every chart function works the same way:
    - it takes the DataFrame and the path of the PNG file to write,
    - it saves the chart to that path,
    - it returns the Figure, and the caller closes it with plt.close(fig).

Keep the function names below, because the tests look for them.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Path(__file__) is the path of this file. The lines below find the course's
# assets folder and the folder this file is in, wherever PyCharm runs it from.
# Leave them as they are. If you copied this file into your own project, see
# the README for the one line to change.
HERE = Path(__file__).resolve().parent
ASSETS = Path(__file__).resolve().parents[3] / "assets"
LOGINS_FILE = ASSETS / "data" / "login_attempts.csv"
SALES_FILE = ASSETS / "data" / "sales.csv"

OPTION = "A"    # TODO: write "A" for the login attempts or "B" for the sales


# ---------------------------------------------------------------------------
# Shared (both options)
# ---------------------------------------------------------------------------

def load_data(path):
    """Read the CSV file at path and return it as a DataFrame."""
    # TODO: one line with pd.read_csv.
    pass


# ---------------------------------------------------------------------------
# Option A: login attempts
# ---------------------------------------------------------------------------

def fails_per_day(df):
    """Return a dictionary: date -> number of failed attempts on that date.

    Every date in df is a key, in date order. A date with no fails has 0.
    Example: {"2026-10-19": 2, "2026-10-20": 0}
    """
    # TODO: make a sorted list of every date in df.
    # TODO: keep only the rows where result is "fail", then count them by date.
    # TODO: build the dictionary. Use 0 for a date that has no fails.
    pass


def fails_per_hour(df, date):
    """Return a dictionary: hour -> number of failed attempts on one date.

    Only hours with at least one fail are keys, in hour order.
    Example: {2: 3, 14: 1}
    """
    # TODO: keep the rows for this date where result is "fail".
    # TODO: count them by hour and build the dictionary.
    pass


def fails_per_ip(df, n=5):
    """Return a list of (ip, count) tuples for the n addresses with most fails.

    The largest count comes first. Addresses with the same count are in
    alphabetical order of the address text.
    Example: [("203.0.113.9", 4), ("192.0.2.1", 1)]
    """
    # TODO: count the failed rows by ip.
    # TODO: build a list of (ip, count) tuples and sort it.
    # TODO: return the first n.
    pass


def chart_fails_per_day(df, path):
    """Save a line chart of failed attempts per day. Return the Figure."""
    # TODO: get the numbers from fails_per_day(df).
    # TODO: fig, ax = plt.subplots(), then ax.plot(...).
    # TODO: title, both axis labels (with units), readable date labels.
    # TODO: fig.savefig(path, dpi=150) and return fig.
    pass


def chart_fails_per_ip(df, path):
    """Save a bar chart of the five addresses with most fails. Return the Figure."""
    # TODO: get the numbers from fails_per_ip(df, 5).
    # TODO: ax.bar or ax.barh. The bars must start at zero.
    # TODO: title, both axis labels (with units).
    # TODO: fig.savefig(path, dpi=150) and return fig.
    pass


# ---------------------------------------------------------------------------
# Option B: sales
# ---------------------------------------------------------------------------

def clean_sales(df):
    """Return a new DataFrame that is ready to analyse.

    Cleaning rule: rows with no units are dropped, because we do not know
    how many were sold. A revenue column is added: units * unit_price.
    The DataFrame given to the function is not changed.
    """
    # TODO: drop the rows with missing units, and take a copy.
    # TODO: add the revenue column to the copy and return the copy.
    pass


def revenue_per_month(df):
    """Return a dictionary: month such as "2026-07" -> revenue in dollars.

    df is a cleaned DataFrame (it has a revenue column). Revenue is rounded
    to 2 decimal places. Months are in date order.
    Example: {"2026-07": 120.5, "2026-08": 64.0}
    """
    # TODO: the month is the first 7 characters of the date.
    # TODO: add up revenue by month and build the dictionary.
    pass


def revenue_per_region(df):
    """Return a dictionary: region -> revenue in dollars, rounded to 2 places.

    df is a cleaned DataFrame (it has a revenue column).
    Example: {"Fremantle": 64.0, "Perth": 120.5}
    """
    # TODO: add up revenue by region and build the dictionary.
    pass


def chart_revenue_per_month(df, path):
    """Save a line chart or bar chart of revenue per month. Return the Figure.

    df is a cleaned DataFrame.
    """
    # TODO: get the numbers from revenue_per_month(df).
    # TODO: fig, ax = plt.subplots(), then ax.plot(...) or ax.bar(...).
    # TODO: title, both axis labels (with units).
    # TODO: fig.savefig(path, dpi=150) and return fig.
    pass


def chart_revenue_per_region(df, path):
    """Save a bar chart of revenue per region. Return the Figure.

    df is a cleaned DataFrame.
    """
    # TODO: get the numbers from revenue_per_region(df).
    # TODO: ax.bar or ax.barh, sorted. The bars must start at zero.
    # TODO: title, both axis labels (with units).
    # TODO: fig.savefig(path, dpi=150) and return fig.
    pass


# ---------------------------------------------------------------------------
# main: print the numbers and build the two charts for your option
# ---------------------------------------------------------------------------

def main():
    # TODO: load the file for your option (LOGINS_FILE or SALES_FILE).
    # TODO: print the numbers from your data functions.
    # TODO: call your two chart functions with HERE / "chart1.png"
    #       and HERE / "chart2.png".
    # TODO: close both figures with plt.close(fig).
    pass


# Leave the next two lines as they are.
if __name__ == "__main__":
    main()
