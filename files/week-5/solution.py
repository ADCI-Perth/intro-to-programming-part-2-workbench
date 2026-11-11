"""Week 5 practice: a web-log summary with Pandas (model solution).

The program reads the course copy of the web log (assets/data/web_log.csv)
into a DataFrame and answers questions about it.

Each function takes a DataFrame and returns a plain Python value
(a number, a dictionary or a list), so the functions are easy to test.
Only main() prints.
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
# The summary functions.
# ---------------------------------------------------------------------------

def load_log(path):
    """Read the CSV file at `path` and return it as a DataFrame."""
    return pd.read_csv(path)


def status_counts(df):
    """Return a dictionary: status code -> number of rows with that status.

    Example: {200: 3, 404: 1}
    """
    return df["status"].value_counts().to_dict()


def missing_sizes(df):
    """Return the number of rows that have no size (NaN), as an int."""
    return int(df["size"].isna().sum())


def total_bytes(df):
    """Return the sum of the size column as an int. A missing size counts as 0."""
    return int(df["size"].fillna(0).sum())


def requests_per_ip(df, n=5):
    """Return the `n` busiest addresses as a list of (ip, count) tuples.

    Sorted by count, largest first. Equal counts are in ascending ip order.
    Example: [("192.0.2.1", 3), ("192.0.2.2", 1)]
    """
    counts = df.groupby("ip").size()
    return sorted_pairs(counts)[:n]


def failed_logins(df):
    """Return failed logins for each address as a list of (ip, count) tuples.

    A failed login is a row where path is "/login" and status is 401.
    Addresses with no failed logins are left out.
    Sorted by count, largest first. Equal counts are in ascending ip order.
    """
    failed = df[(df["path"] == "/login") & (df["status"] == 401)]
    counts = failed.groupby("ip").size()
    return sorted_pairs(counts)


def not_found_paths(df, n=5):
    """Return the `n` most requested paths that gave status 404.

    The result is a list of (path, count) tuples.
    Sorted by count, largest first. Equal counts are in ascending path order.
    """
    not_found = df[df["status"] == 404]
    counts = not_found.groupby("path").size()
    return sorted_pairs(counts)[:n]


def requests_per_hour(df):
    """Return a dictionary: hour (an int from 0 to 23) -> number of requests.

    The hour is the first two characters of the time column, so "07:13:45"
    is hour 7. Hours with no requests are left out. The keys are in
    ascending order.
    Example: {7: 2, 14: 1}
    """
    hours = df["time"].str[:2].astype(int)
    return hours.value_counts().sort_index().to_dict()


def suspicious_ips(df, threshold=10):
    """Return a sorted list of addresses worth a closer look.

    An address is in the list when it has at least `threshold` rows
    with status 401 or 404.
    Example: ["203.0.113.45", "203.0.113.77"]
    """
    bad = df[df["status"].isin([401, 404])]
    counts = bad.groupby("ip").size()
    return sorted(counts[counts >= threshold].index)


def main():
    df = load_log(LOG_FILE)

    print("Web-log summary")
    print("===============")
    print(f"Rows: {len(df)}")
    print(f"Rows with no size: {missing_sizes(df)}")
    print(f"Total bytes sent (missing size counted as 0): {total_bytes(df):,}")

    print()
    print("Requests for each status code")
    for status, count in sorted(status_counts(df).items()):
        print(f"  {status}: {count}")

    print()
    print("Busiest addresses")
    for ip, count in requests_per_ip(df):
        print(f"  {ip:<15} {count:>3}")

    print()
    print("Failed logins (/login with status 401)")
    for ip, count in failed_logins(df):
        print(f"  {ip:<15} {count:>3}")

    print()
    print("Paths most often not found (status 404)")
    for path, count in not_found_paths(df):
        print(f"  {path:<15} {count:>3}")

    print()
    print("Requests for each hour")
    for hour, count in requests_per_hour(df).items():
        print(f"  {hour:02}:00  {count:>3}")

    print()
    print("Addresses with 10 or more 401 or 404 responses")
    for ip in suspicious_ips(df):
        print(f"  {ip}")
    print()
    print("A pattern in a log is a reason to look closer. It is not proof.")


if __name__ == "__main__":
    main()
