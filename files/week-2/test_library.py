"""Tests for the Week 2 library (Part B): library.py, and main.py as a menu.

To test your own work, set MINI_PROJECT_DIR to the folder holding your
library.py and main.py (see the README). Without it, the tests use the
model solution in solution/.

Every file these tests write goes into pytest's temporary folder. The menu
tests copy library.py and main.py there first, so library.json is never
written into your own folder or the course folder.
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

SOLUTION_DIR = Path(os.environ.get("MINI_PROJECT_DIR") or Path(__file__).parent / "solution")
sys.path.insert(0, str(SOLUTION_DIR))

from library import Book, Library  # noqa: E402


@pytest.fixture
def library():
    lib = Library()
    lib.add_book(Book("Dune", "Frank Herbert", "111"))
    lib.add_book(Book("Emma", "Jane Austen", "222"))
    lib.add_book(Book("Persuasion", "Jane Austen", "333"))
    return lib


# ---- The Part 1 interface still works ---------------------------------------

def test_search_ignores_case(library):
    assert [b.isbn for b in library.search("dUnE")] == ["111"]
    assert {b.isbn for b in library.search("austen")} == {"222", "333"}
    assert library.search("zzz") == []


def test_lend_and_available(library):
    library.lend("111")
    assert library.books["111"].on_loan is True
    assert {b.isbn for b in library.available_books()} == {"222", "333"}


def test_lend_and_return_errors(library):
    with pytest.raises(KeyError):
        library.lend("999")
    with pytest.raises(ValueError):
        library.return_book("111")
    library.lend("111")
    with pytest.raises(ValueError):
        library.lend("111")
    library.return_book("111")
    assert library.books["111"].on_loan is False


def test_book_str_matches_part_1():
    book = Book("Dune", "Frank Herbert", "111")
    assert str(book) == "Dune by Frank Herbert (111) - available"
    book.on_loan = True
    assert str(book) == "Dune by Frank Herbert (111) - on loan"


# ---- to_dict and from_dict --------------------------------------------------

def test_to_dict():
    book = Book("Dune", "Frank Herbert", "111")
    assert book.to_dict() == {
        "title": "Dune",
        "author": "Frank Herbert",
        "isbn": "111",
        "on_loan": False,
    }


def test_from_dict_restores_on_loan():
    data = {"title": "Emma", "author": "Jane Austen", "isbn": "222", "on_loan": True}
    book = Book.from_dict(data)
    assert isinstance(book, Book)
    assert (book.title, book.author, book.isbn) == ("Emma", "Jane Austen", "222")
    assert book.on_loan is True


def test_dict_round_trip():
    book = Book("Dune", "Frank Herbert", "111")
    book.on_loan = True
    copy = Book.from_dict(book.to_dict())
    assert str(copy) == str(book)


# ---- save and load ------------------------------------------------------------

def test_save_writes_a_json_list(library, tmp_path):
    path = tmp_path / "books.json"
    library.lend("222")
    library.save(path)
    with open(path, encoding="utf-8") as file:
        text = file.read()
    records = json.loads(text)
    assert isinstance(records, list) and len(records) == 3
    assert {"title": "Emma", "author": "Jane Austen", "isbn": "222", "on_loan": True} in records
    assert "\n  " in text  # indent=2 puts each value on its own line


def test_save_then_load_round_trip(library, tmp_path):
    path = tmp_path / "books.json"
    library.lend("111")
    library.save(path)
    loaded = Library.load(path)
    assert isinstance(loaded, Library)
    assert sorted(loaded.books) == ["111", "222", "333"]
    assert loaded.books["111"].on_loan is True
    assert loaded.books["333"].on_loan is False
    assert {b.isbn for b in loaded.available_books()} == {"222", "333"}


def test_load_missing_file_gives_empty_library(tmp_path):
    loaded = Library.load(tmp_path / "no_such_file.json")
    assert isinstance(loaded, Library)
    assert loaded.books == {}


def test_save_and_load_keep_non_ascii_text(tmp_path):
    path = tmp_path / "books.json"
    lib = Library()
    lib.add_book(Book("Café Stories", "Zoë Example", "444"))
    lib.save(path)
    assert Library.load(path).books["444"].title == "Café Stories"


# ---- main.py as a menu, run in a temporary copy -------------------------------

@pytest.fixture
def project(tmp_path):
    """Copy library.py and main.py into a temporary folder and return it."""
    for name in ("library.py", "main.py"):
        shutil.copy(SOLUTION_DIR / name, tmp_path / name)
    return tmp_path


def run_menu(folder, *answers):
    """Run main.py in folder, typing each answer on its own line."""
    result = subprocess.run(
        [sys.executable, "main.py"],
        cwd=folder,
        input="\n".join(answers) + "\n",
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0, result.stderr
    return result.stdout


def test_menu_quit_saves_the_books(project):
    out = run_menu(project, "1", "Dune", "Frank Herbert", "111", "6")
    assert "Book added." in out
    assert "Goodbye. Books saved." in out
    with open(project / "library.json", encoding="utf-8") as file:
        records = json.load(file)
    assert records == [
        {"title": "Dune", "author": "Frank Herbert", "isbn": "111", "on_loan": False}
    ]


def test_menu_books_survive_a_second_run(project):
    run_menu(project, "1", "Dune", "Frank Herbert", "111", "1", "Emma", "Jane Austen", "222", "3", "111", "6")
    out = run_menu(project, "2", "6")
    assert "Emma by Jane Austen (222) - available" in out
    assert "Dune by Frank Herbert" not in out  # Dune is still on loan
    out = run_menu(project, "4", "111", "2", "6")
    assert "Dune by Frank Herbert (111) - available" in out


def test_menu_first_run_starts_empty(project):
    out = run_menu(project, "2", "6")
    assert "No books available." in out


def test_menu_still_handles_bad_input(project):
    out = run_menu(project, "9", "3", "999", "6")
    assert "Please enter a number from 1 to 6." in out
    assert "No book with that ISBN." in out
