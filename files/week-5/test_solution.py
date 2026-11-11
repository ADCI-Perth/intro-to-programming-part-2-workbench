"""Tests for the Week 5 practice task.

To test your own work, change the import below from `solution` to `starter`.

Most tests build a small DataFrame by hand, so you can work out the right
answer yourself. The last few tests use the real course file.
"""

import pandas as pd

import solution as log


def make_log():
    """Return a small hand-made log with eight rows."""
    rows = [
        # ip, time, path, status, size
        ("192.0.2.1", "07:15:00", "/index.html", 200, 100),
        ("192.0.2.1", "07:45:10", "/login", 401, 50),
        ("192.0.2.1", "09:05:30", "/login", 401, 50),
        ("192.0.2.2", "09:10:00", "/login", 200, 80),
        ("192.0.2.2", "09:20:00", "/missing.html", 404, 30),
        ("192.0.2.3", "14:00:00", "/index.html", 304, None),
        ("192.0.2.3", "14:30:00", "/missing.html", 404, 30),
        ("192.0.2.3", "23:59:59", "/admin", 404, 30),
    ]
    df = pd.DataFrame(rows, columns=["ip", "time", "path", "status", "size"])
    df["date"] = "09/Nov/2026"
    df["method"] = "GET"
    return df


def test_sorted_pairs_breaks_ties_by_label():
    counts = pd.Series({"b": 2, "a": 2, "c": 5})
    assert log.sorted_pairs(counts) == [("c", 5), ("a", 2), ("b", 2)]


def test_load_log_reads_a_csv(tmp_path):
    path = tmp_path / "tiny.csv"
    path.write_text(
        "ip,date,time,method,path,status,size\n"
        "192.0.2.1,09/Nov/2026,07:15:00,GET,/index.html,200,100\n"
        "192.0.2.2,09/Nov/2026,07:16:00,GET,/index.html,304,\n"
    )
    df = log.load_log(path)
    assert df.shape == (2, 7)
    assert list(df.columns) == ["ip", "date", "time", "method", "path", "status", "size"]


def test_status_counts():
    assert log.status_counts(make_log()) == {200: 2, 401: 2, 404: 3, 304: 1}


def test_missing_sizes():
    assert log.missing_sizes(make_log()) == 1


def test_total_bytes_treats_missing_as_zero():
    total = log.total_bytes(make_log())
    assert total == 370
    assert type(total) is int


def test_requests_per_ip_sorts_and_breaks_ties():
    df = make_log()
    # 192.0.2.1 and 192.0.2.3 both have 3 rows, so the lower address is first.
    assert log.requests_per_ip(df) == [("192.0.2.1", 3), ("192.0.2.3", 3), ("192.0.2.2", 2)]
    assert log.requests_per_ip(df, n=1) == [("192.0.2.1", 3)]


def test_failed_logins_needs_login_path_and_401():
    # The 200 on /login and the 404 rows must not be counted.
    assert log.failed_logins(make_log()) == [("192.0.2.1", 2)]


def test_not_found_paths():
    df = make_log()
    assert log.not_found_paths(df) == [("/missing.html", 2), ("/admin", 1)]
    assert log.not_found_paths(df, n=1) == [("/missing.html", 2)]


def test_requests_per_hour_uses_int_hours():
    assert log.requests_per_hour(make_log()) == {7: 2, 9: 3, 14: 2, 23: 1}


def test_suspicious_ips_uses_threshold():
    df = make_log()
    # Rows with status 401 or 404: 192.0.2.1 has 2, 192.0.2.2 has 1, 192.0.2.3 has 2.
    assert log.suspicious_ips(df, threshold=2) == ["192.0.2.1", "192.0.2.3"]
    assert log.suspicious_ips(df, threshold=1) == ["192.0.2.1", "192.0.2.2", "192.0.2.3"]
    assert log.suspicious_ips(df) == []


def test_functions_do_not_change_the_dataframe():
    df = make_log()
    before = df.copy()
    log.total_bytes(df)
    log.requests_per_hour(df)
    log.suspicious_ips(df)
    assert df.equals(before)


# ---------------------------------------------------------------------------
# Tests on the real course file, assets/data/web_log.csv
# ---------------------------------------------------------------------------

def test_real_log_size_and_status_counts():
    df = log.load_log(log.LOG_FILE)
    assert df.shape == (200, 7)
    assert log.status_counts(df) == {200: 143, 401: 27, 404: 16, 304: 12, 500: 2}
    assert log.missing_sizes(df) == 12
    assert log.total_bytes(df) == 933301


def test_real_log_busiest_addresses_have_a_tie():
    df = log.load_log(log.LOG_FILE)
    top = log.requests_per_ip(df, n=3)
    assert top == [("198.51.100.56", 22), ("203.0.113.45", 22), ("192.0.2.15", 20)]


def test_real_log_failed_logins_and_suspicious_ips():
    df = log.load_log(log.LOG_FILE)
    assert log.failed_logins(df)[0] == ("203.0.113.45", 22)
    assert log.not_found_paths(df, n=1) == [("/old-page.html", 6)]
    assert log.requests_per_hour(df)[2] == 22
    assert log.suspicious_ips(df) == ["203.0.113.45", "203.0.113.77"]
