"""Tests for the Week 6 capstone.

To test your own work, change the import below from `solution` to `starter`.

Tests named test_a_... are for Option A (login attempts).
Tests named test_b_... are for Option B (sales).
You complete one option, so run only your group:

    python -m pytest weeks/week-6/practice -k "test_a"
    python -m pytest weeks/week-6/practice -k "test_b"
"""

from pathlib import Path

import matplotlib

# "Agg" tells Matplotlib to draw into files only, so no window opens during
# the tests. This line must come before pyplot or the solution is imported.
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

import solution as cap

ASSETS = Path(__file__).resolve().parents[3] / "assets"
LOGINS_FILE = ASSETS / "data" / "login_attempts.csv"
SALES_FILE = ASSETS / "data" / "sales.csv"


def small_logins():
    """Seven hand-made login attempts over three days. The second date has no fails."""
    return pd.DataFrame({
        "date": ["2026-03-01", "2026-03-01", "2026-03-01", "2026-03-02",
                 "2026-03-03", "2026-03-03", "2026-03-03"],
        "hour": [9, 9, 14, 10, 2, 2, 3],
        "user": ["user01", "user02", "user01", "user02",
                 "admin", "admin", "user01"],
        "ip": ["192.0.2.5", "192.0.2.9", "192.0.2.5", "192.0.2.9",
               "203.0.113.8", "203.0.113.8", "192.0.2.5"],
        "result": ["fail", "success", "fail", "success",
                   "fail", "fail", "fail"],
    })


def small_sales():
    """Five hand-made sales rows over two months. One row has no units."""
    return pd.DataFrame({
        "date": ["2026-01-05", "2026-01-20", "2026-02-03", "2026-02-10",
                 "2026-02-11"],
        "region": ["Perth", "Fremantle", "Perth", "Fremantle", "Perth"],
        "product": ["Notebook", "Pen pack", "Notebook", "Pen pack",
                    "Notebook"],
        "units": [2, 3, None, 5, 4],
        "unit_price": [6.50, 4.00, 6.50, 4.00, 6.50],
    })


def check_chart(fig, path):
    """Checks that every chart must pass. Returns the chart's axes."""
    assert fig is not None, "the chart function must return the Figure"
    assert Path(path).exists(), "the PNG file was not saved"
    assert Path(path).stat().st_size > 0, "the PNG file is empty"
    ax = fig.axes[0]
    assert ax.get_title() != "", "the chart needs a title"
    assert ax.get_xlabel() != "", "the x axis needs a label"
    assert ax.get_ylabel() != "", "the y axis needs a label"
    return ax


def bars_start_at_zero(ax):
    """True when the chart has bars and the number axis starts at zero."""
    has_bars = len(ax.patches) > 0
    return has_bars and (ax.get_ylim()[0] == 0 or ax.get_xlim()[0] == 0)


# ---------------------------------------------------------------------------
# Option A: login attempts
# ---------------------------------------------------------------------------

def test_a_load_data_logins():
    df = cap.load_data(LOGINS_FILE)
    assert len(df) == 563
    assert list(df.columns) == ["date", "hour", "user", "ip", "result"]


def test_a_fails_per_day_small_includes_days_with_no_fails():
    result = cap.fails_per_day(small_logins())
    assert dict(result) == {"2026-03-01": 2, "2026-03-02": 0, "2026-03-03": 3}
    assert list(result) == ["2026-03-01", "2026-03-02", "2026-03-03"]


def test_a_fails_per_day_real_file():
    result = dict(cap.fails_per_day(pd.read_csv(LOGINS_FILE)))
    assert len(result) == 14
    assert result["2026-10-27"] == 91
    assert result["2026-10-24"] == 0
    other_days = [n for date, n in result.items() if date != "2026-10-27"]
    assert min(other_days) == 0
    assert max(other_days) == 6


def test_a_fails_per_hour():
    assert cap.fails_per_hour(small_logins(), "2026-03-03") == {2: 2, 3: 1}
    assert cap.fails_per_hour(small_logins(), "2026-03-02") == {}
    real = cap.fails_per_hour(pd.read_csv(LOGINS_FILE), "2026-10-27")
    assert real == {1: 29, 2: 47, 3: 14, 13: 1}


def test_a_fails_per_ip():
    small = small_logins()
    assert cap.fails_per_ip(small) == [("192.0.2.5", 3), ("203.0.113.8", 2)]
    assert cap.fails_per_ip(small, 1) == [("192.0.2.5", 3)]
    real = cap.fails_per_ip(pd.read_csv(LOGINS_FILE))
    assert len(real) == 5
    assert real[0] == ("203.0.113.45", 90)
    assert real[1] == ("192.0.2.20", 6)
    assert real[2] == ("192.0.2.21", 4)     # a tie on 4: alphabetical order


def test_a_chart_fails_per_day(tmp_path):
    path = tmp_path / "chart1.png"
    fig = cap.chart_fails_per_day(pd.read_csv(LOGINS_FILE), path)
    ax = check_chart(fig, path)
    assert len(ax.lines) > 0, "this chart must be a line chart"
    plt.close(fig)


def test_a_chart_fails_per_ip(tmp_path):
    path = tmp_path / "chart2.png"
    fig = cap.chart_fails_per_ip(pd.read_csv(LOGINS_FILE), path)
    ax = check_chart(fig, path)
    assert bars_start_at_zero(ax), "a bar chart whose bars start at zero"
    plt.close(fig)


# ---------------------------------------------------------------------------
# Option B: sales
# ---------------------------------------------------------------------------

def test_b_load_data_sales():
    df = cap.load_data(SALES_FILE)
    assert len(df) == 571
    assert list(df.columns) == ["date", "region", "product", "units",
                                "unit_price"]
    assert df["units"].isna().sum() == 6


def test_b_clean_sales_small():
    raw = small_sales()
    clean = cap.clean_sales(raw)
    assert len(clean) == 4
    assert list(clean["revenue"]) == [13.0, 12.0, 20.0, 26.0]
    assert len(raw) == 5, "clean_sales must not change the DataFrame it is given"
    assert "revenue" not in raw.columns


def test_b_clean_sales_real_file():
    clean = cap.clean_sales(pd.read_csv(SALES_FILE))
    assert len(clean) == 565
    assert clean["units"].isna().sum() == 0
    assert round(float(clean["revenue"].sum()), 2) == 41863.50


def test_b_revenue_per_month():
    small = cap.clean_sales(small_sales())
    assert cap.revenue_per_month(small) == {"2026-01": 25.0, "2026-02": 46.0}
    real = cap.revenue_per_month(cap.clean_sales(pd.read_csv(SALES_FILE)))
    assert real == {"2026-07": 11411.50, "2026-08": 12359.00,
                    "2026-09": 18093.00}


def test_b_revenue_per_region():
    small = cap.clean_sales(small_sales())
    assert cap.revenue_per_region(small) == {"Perth": 39.0, "Fremantle": 32.0}
    real = cap.revenue_per_region(cap.clean_sales(pd.read_csv(SALES_FILE)))
    assert real == {"Perth": 18754.50, "Fremantle": 12497.00,
                    "Joondalup": 10612.00}


def test_b_chart_revenue_per_month(tmp_path):
    path = tmp_path / "chart1.png"
    clean = cap.clean_sales(pd.read_csv(SALES_FILE))
    fig = cap.chart_revenue_per_month(clean, path)
    ax = check_chart(fig, path)
    assert len(ax.lines) > 0 or len(ax.patches) > 0
    plt.close(fig)


def test_b_chart_revenue_per_region(tmp_path):
    path = tmp_path / "chart2.png"
    clean = cap.clean_sales(pd.read_csv(SALES_FILE))
    fig = cap.chart_revenue_per_region(clean, path)
    ax = check_chart(fig, path)
    assert bars_start_at_zero(ax), "a bar chart whose bars start at zero"
    plt.close(fig)
