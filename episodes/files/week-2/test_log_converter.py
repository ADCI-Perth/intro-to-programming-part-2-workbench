"""Tests for the Week 2 web-log converter (Part A): log_converter.py.

To test your own work, set MINI_PROJECT_DIR to the folder holding your
log_converter.py (see the README). Without it, the tests use the model
solution in solution/.

Every file these tests write goes into pytest's temporary folder.
"""

import csv
import os
import shutil
import subprocess
import sys
from pathlib import Path

SOLUTION_DIR = Path(os.environ.get("MINI_PROJECT_DIR") or Path(__file__).parent / "solution")
sys.path.insert(0, str(SOLUTION_DIR))

import log_converter as lc  # noqa: E402

ASSETS = Path(__file__).resolve().parents[3] / "assets"
LOG_FILE = ASSETS / "files" / "web_log.txt"
EXPECTED_CSV = ASSETS / "data" / "web_log.csv"

GOOD_LINE = '192.0.2.33 - - [09/Nov/2026:07:13:45 +0800] "GET /contact.html HTTP/1.1" 200 2260'
NO_SIZE_LINE = '198.51.100.48 - - [09/Nov/2026:12:04:23 +0800] "GET /index.html HTTP/1.1" 304 -'
LOGIN_LINE = '192.0.2.10 - - [09/Nov/2026:09:06:20 +0800] "POST /login HTTP/1.1" 401 512'


def read_rows(path):
    """Return every row of a CSV file as a list of lists."""
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.reader(file))


# ---- parse_line -----------------------------------------------------------

def test_parse_line_good_line():
    assert lc.parse_line(GOOD_LINE) == {
        "ip": "192.0.2.33",
        "date": "09/Nov/2026",
        "time": "07:13:45",
        "method": "GET",
        "path": "/contact.html",
        "status": "200",
        "size": "2260",
    }


def test_parse_line_copes_with_newline_at_the_end():
    record = lc.parse_line(LOGIN_LINE + "\n")
    assert record["method"] == "POST"
    assert record["status"] == "401"
    assert record["size"] == "512"


def test_parse_line_missing_size_is_empty_string():
    assert lc.parse_line(NO_SIZE_LINE)["size"] == ""


def test_parse_line_all_values_are_strings():
    record = lc.parse_line(GOOD_LINE)
    assert sorted(record) == ["date", "ip", "method", "path", "size", "status", "time"]
    assert all(type(value) is str for value in record.values())


def test_parse_line_blank_or_short_line_gives_none():
    assert lc.parse_line("") is None
    assert lc.parse_line("\n") is None
    assert lc.parse_line("192.0.2.33 - - broken line") is None


# ---- read_log, write_csv, count_status ------------------------------------

def test_read_log_skips_bad_lines(tmp_path):
    log = tmp_path / "small.txt"
    log.write_text(
        GOOD_LINE + "\n\n" + "not a log line\n" + NO_SIZE_LINE + "\n",
        encoding="utf-8",
    )
    records = lc.read_log(log)
    assert [record["status"] for record in records] == ["200", "304"]


def test_read_log_real_file_has_200_records():
    assert len(lc.read_log(LOG_FILE)) == 200


def test_write_csv_header_and_rows(tmp_path):
    out = tmp_path / "out.csv"
    lc.write_csv([lc.parse_line(GOOD_LINE), lc.parse_line(NO_SIZE_LINE)], out)
    assert read_rows(out) == [
        ["ip", "date", "time", "method", "path", "status", "size"],
        ["192.0.2.33", "09/Nov/2026", "07:13:45", "GET", "/contact.html", "200", "2260"],
        ["198.51.100.48", "09/Nov/2026", "12:04:23", "GET", "/index.html", "304", ""],
    ]


def test_write_csv_has_no_blank_lines_between_rows(tmp_path):
    out = tmp_path / "out.csv"
    lc.write_csv([lc.parse_line(GOOD_LINE), lc.parse_line(LOGIN_LINE)], out)
    text = out.read_bytes().decode("utf-8")
    assert "\r\r\n" not in text and "\n\n" not in text


def test_count_status():
    records = [lc.parse_line(line) for line in (GOOD_LINE, LOGIN_LINE, GOOD_LINE)]
    assert lc.count_status(records) == {"200": 2, "401": 1}
    assert lc.count_status([]) == {}


def test_count_status_real_file():
    counts = lc.count_status(lc.read_log(LOG_FILE))
    assert counts == {"200": 143, "401": 27, "404": 16, "304": 12, "500": 2}


def test_converted_log_matches_the_course_csv(tmp_path):
    out = tmp_path / "web_log.csv"
    lc.write_csv(lc.read_log(LOG_FILE), out)
    assert read_rows(out) == read_rows(EXPECTED_CSV)


# ---- main, run as a program in a temporary copy ----------------------------

def run_main_in(folder):
    """Copy log_converter.py into folder, run it there and return the output."""
    shutil.copy(SOLUTION_DIR / "log_converter.py", folder / "log_converter.py")
    result = subprocess.run(
        [sys.executable, "log_converter.py"],
        cwd=folder,
        capture_output=True,
        text=True,
        timeout=20,
    )
    assert result.returncode == 0, result.stderr
    return result.stdout


def test_main_converts_the_log_next_to_it(tmp_path):
    shutil.copy(LOG_FILE, tmp_path / "web_log.txt")
    out = run_main_in(tmp_path)
    assert "200 lines" in out
    assert "143" in out and "27" in out
    assert read_rows(tmp_path / "web_log.csv") == read_rows(EXPECTED_CSV)


def test_main_without_the_log_prints_a_message(tmp_path):
    out = run_main_in(tmp_path)
    assert "Cannot find web_log.txt" in out
    assert not (tmp_path / "web_log.csv").exists()
