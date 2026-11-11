"""Week 5 practice: a web-log summary with Pandas.

The program reads the course copy of the web log (assets/data/web_log.csv)
into a DataFrame and answers questions about it.

Each function takes a DataFrame and returns a plain Python value
(a number, a dictionary or a list), so the functions are easy to test.
Only main() prints.

Fill in each TODO. Keep the function names, because the tests look for them.
"""

from pathlib import Path

import pandas as pd

# Path(__file__) is this file. parents[3] is the top folder of the course.
# These two lines find the web log from any working folder. Leave them as is.
ASSETS = Path(__file__).resolve().parents[3] / "assets"
LOG_FILE = ASSETS / "data" / "web_log.csv"


# ---------------------------------------------------------------------------
# Given helper (already works). Read it, then use it in your own functions.
# ---------------------------------------------------------------------------

def sorted_pairs(counts):
    """Turn a Series of counts into a sorted list of (label, count) tuples.

    `counts` is a Series such as the result of df.groupby("ip").size().
    Its labels (the index) are the group names and its values are the counts.

    The list is sorted by count, largest first. When two counts are equal,
    the labels are in ascending (a to z) order. Each count is a plain int.

    Example: a Series with b -> 2, a -> 2, c -> 5
             gives [("c", 5), ("a", 2), ("b", 2)]
    """
    pairs = [(label, int(count)) for label, count in counts.items()]
    return sorted(pairs, key=lambda pair: (-pair[1], pair[0]))


# ---------------------------------------------------------------------------
# Your functions.
# ---------------------------------------------------------------------------

def load_log(path):
    """Read the CSV file at `path` and return it as a DataFrame."""
    # TODO: use pd.read_csv
    pass


def status_counts(df):
    """Return a dictionary: status code -> number of rows with that status.

    Example: {200: 3, 404: 1}
    """
    # TODO: use value_counts() on the status column, then .to_dict()
    pass


def missing_sizes(df):
    """Return the number of rows that have no size (NaN), as an int."""
    # TODO: use isna() and sum(), then int(...)
    pass


def total_bytes(df):
    """Return the sum of the size column as an int. A missing size counts as 0."""
    # TODO: use fillna(0) and sum(), then int(...)
    pass


def requests_per_ip(df, n=5):
    """Return the `n` busiest addresses as a list of (ip, count) tuples.

    Sorted by count, largest first. Equal counts are in ascending ip order.
    Example: [("192.0.2.1", 3), ("192.0.2.2", 1)]
    """
    # TODO: group by ip, count with size(), pass the result to sorted_pairs,
    #       then slice the list to keep the first n
    pass


def failed_logins(df):
    """Return failed logins for each address as a list of (ip, count) tuples.

    A failed login is a row where path is "/login" and status is 401.
    Addresses with no failed logins are left out.
    Sorted by count, largest first. Equal counts are in ascending ip order.
    """
    # TODO: filter with two conditions joined by &, then group by ip,
    #       count with size() and use sorted_pairs
    pass


def not_found_paths(df, n=5):
    """Return the `n` most requested paths that gave status 404.

    The result is a list of (path, count) tuples.
    Sorted by count, largest first. Equal counts are in ascending path order.
    """
    # TODO: filter to status 404, group by path, count, use sorted_pairs,
    #       then keep the first n
    pass


def requests_per_hour(df):
    """Return a dictionary: hour (an int from 0 to 23) -> number of requests.

    The hour is the first two characters of the time column, so "07:13:45"
    is hour 7. Hours with no requests are left out. The keys are in
    ascending order.
    Example: {7: 2, 14: 1}
    """
    # TODO: use .str[:2] and .astype(int) on the time column,
    #       then value_counts(), sort_index() and to_dict()
    pass


def suspicious_ips(df, threshold=10):
    """Return a sorted list of addresses worth a closer look.

    An address is in the list when it has at least `threshold` rows
    with status 401 or 404.
    Example: ["203.0.113.45", "203.0.113.77"]
    """
    # TODO: filter with isin([401, 404]), group by ip and count with size(),
    #       keep the counts that are >= threshold, then return
    #       sorted(...) of the labels that are left (use .index)
    pass


def main():
    df = load_log(LOG_FILE)

    print("Web-log summary")
    print("===============")
    # TODO: print a tidy report that uses every function above.
    #       See the example run in README.md.


if __name__ == "__main__":
    main()
