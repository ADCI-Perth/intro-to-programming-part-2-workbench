"""Week 6 capstone: two charts and a written finding (model solution).

This model solution completes BOTH options so the tests for both pass.
You complete only ONE option in your own starter.py.

Option A (security): login_attempts.csv, columns date,hour,user,ip,result
Option B (data):     sales.csv, columns date,region,product,units,unit_price

Design used by every chart function:
    - it takes the DataFrame and the path of the PNG file to write,
    - it saves the chart to that path,
    - it returns the Figure, and the caller closes it with plt.close(fig).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Path(__file__) is the path of this file. The lines below find the course's
# assets folder and the folder this file is in, wherever PyCharm runs it from.
HERE = Path(__file__).resolve().parent
ASSETS = Path(__file__).resolve().parents[3] / "assets"
LOGINS_FILE = ASSETS / "data" / "login_attempts.csv"
SALES_FILE = ASSETS / "data" / "sales.csv"

OPTION = "A"    # "A" for the login attempts, "B" for the sales


# ---------------------------------------------------------------------------
# Shared
# ---------------------------------------------------------------------------

def load_data(path):
    """Read the CSV file at path and return it as a DataFrame."""
    return pd.read_csv(path)


# ---------------------------------------------------------------------------
# Option A: login attempts
# ---------------------------------------------------------------------------

def fails_per_day(df):
    """Return a dictionary: date -> number of failed attempts on that date.

    Every date in df is a key, in date order. A date with no fails has 0.
    """
    dates = sorted(df["date"].unique())
    fails = df[df["result"] == "fail"]
    counts = fails.groupby("date").size()
    return {date: int(counts.get(date, 0)) for date in dates}


def fails_per_hour(df, date):
    """Return a dictionary: hour -> number of failed attempts on one date.

    Only hours with at least one fail are keys, in hour order.
    """
    rows = df[(df["date"] == date) & (df["result"] == "fail")]
    counts = rows.groupby("hour").size()
    return {int(hour): int(count) for hour, count in counts.items()}


def fails_per_ip(df, n=5):
    """Return a list of (ip, count) tuples for the n addresses with most fails.

    The largest count comes first. Addresses with the same count are in
    alphabetical order of the address text.
    """
    fails = df[df["result"] == "fail"]
    counts = fails.groupby("ip").size()
    pairs = [(ip, int(count)) for ip, count in counts.items()]
    pairs.sort(key=lambda pair: (-pair[1], pair[0]))
    return pairs[:n]


def chart_fails_per_day(df, path):
    """Save a line chart of failed attempts per day. Return the Figure."""
    per_day = fails_per_day(df)
    dates = list(per_day.keys())
    counts = list(per_day.values())

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(dates, counts, marker="o")
    ax.set_title("Failed login attempts per day")
    ax.set_xlabel("Date")
    ax.set_ylabel("Failed attempts (count)")
    ax.set_ylim(bottom=0)
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    return fig


def chart_fails_per_ip(df, path):
    """Save a bar chart of the five addresses with most fails. Return the Figure."""
    pairs = fails_per_ip(df, 5)
    pairs.reverse()                     # barh draws the first item at the bottom
    addresses = [ip for ip, count in pairs]
    counts = [count for ip, count in pairs]

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.barh(addresses, counts)
    ax.set_title("Failed login attempts by IP address (top 5)")
    ax.set_xlabel("Failed attempts (count)")
    ax.set_ylabel("IP address")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    return fig


# ---------------------------------------------------------------------------
# Option B: sales
# ---------------------------------------------------------------------------

def clean_sales(df):
    """Return a new DataFrame that is ready to analyse.

    Cleaning rule: rows with no units are dropped, because we do not know
    how many were sold. A revenue column is added: units * unit_price.
    The DataFrame given to the function is not changed.
    """
    clean = df.dropna(subset=["units"]).copy()
    clean["revenue"] = clean["units"] * clean["unit_price"]
    return clean


def revenue_per_month(df):
    """Return a dictionary: month such as "2026-07" -> revenue in dollars.

    df is a cleaned DataFrame (it has a revenue column). Revenue is rounded
    to 2 decimal places. Months are in date order.
    """
    months = df["date"].str[:7]
    totals = df.groupby(months)["revenue"].sum()
    return {month: round(float(total), 2) for month, total in totals.items()}


def revenue_per_region(df):
    """Return a dictionary: region -> revenue in dollars, rounded to 2 places.

    df is a cleaned DataFrame (it has a revenue column).
    """
    totals = df.groupby("region")["revenue"].sum()
    return {region: round(float(total), 2) for region, total in totals.items()}


def chart_revenue_per_month(df, path):
    """Save a line chart of revenue per month. Return the Figure.

    df is a cleaned DataFrame.
    """
    per_month = revenue_per_month(df)
    months = list(per_month.keys())
    totals = list(per_month.values())

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(months, totals, marker="o")
    ax.set_title("Revenue per month, July to September 2026")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue ($)")
    ax.set_ylim(bottom=0)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    return fig


def chart_revenue_per_region(df, path):
    """Save a bar chart of revenue per region. Return the Figure.

    df is a cleaned DataFrame. The tallest bar is on the left.
    """
    per_region = revenue_per_region(df)
    pairs = sorted(per_region.items(), key=lambda pair: pair[1], reverse=True)
    regions = [region for region, total in pairs]
    totals = [total for region, total in pairs]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(regions, totals)
    ax.set_title("Revenue per region, July to September 2026")
    ax.set_xlabel("Region")
    ax.set_ylabel("Revenue ($)")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    return fig


# ---------------------------------------------------------------------------
# main: print the numbers and build the two charts for the chosen option
# ---------------------------------------------------------------------------

def main():
    if OPTION == "A":
        df = load_data(LOGINS_FILE)
        print("Rows:", len(df))
        print("Fails per day:", fails_per_day(df))
        print("Busiest addresses:", fails_per_ip(df))
        fig1 = chart_fails_per_day(df, HERE / "chart1.png")
        fig2 = chart_fails_per_ip(df, HERE / "chart2.png")
    else:
        df = load_data(SALES_FILE)
        print("Rows:", len(df))
        clean = clean_sales(df)
        print("Rows after cleaning:", len(clean))
        print("Revenue per month:", revenue_per_month(clean))
        print("Revenue per region:", revenue_per_region(clean))
        fig1 = chart_revenue_per_month(clean, HERE / "chart1.png")
        fig2 = chart_revenue_per_region(clean, HERE / "chart2.png")
    plt.close(fig1)
    plt.close(fig2)
    print("Saved chart1.png and chart2.png in", HERE)


if __name__ == "__main__":
    main()
