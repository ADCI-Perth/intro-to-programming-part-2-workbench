"""Library loan manager: Week 2 model solution (saved to a JSON file).

The same Book and Library classes as Part 1 Week 6, with four additions:
Book.to_dict, Book.from_dict, Library.save and Library.load.
"""

import json


class Book:
    """One book. isbn is its unique identifier."""

    def __init__(self, title, author, isbn):
        """Store the details and mark the book as not on loan."""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.on_loan = False

    def __str__(self):
        """Return a one-line description, such as 'Dune by ... - available'."""
        status = "on loan" if self.on_loan else "available"
        return f"{self.title} by {self.author} ({self.isbn}) - {status}"

    def to_dict(self):
        """Return the book as a dictionary that JSON can store."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "on_loan": self.on_loan,
        }

    @classmethod
    def from_dict(cls, data):
        """Build a Book from a dictionary made by to_dict.

        KeyError if a key is missing. ValueError if on_loan is not True or False.
        """
        if type(data["on_loan"]) is not bool:
            raise ValueError("on_loan must be true or false")
        book = cls(data["title"], data["author"], data["isbn"])
        book.on_loan = data["on_loan"]
        return book


class Library:
    """A collection of books, stored in a dictionary keyed by isbn."""

    def __init__(self):
        """Start with no books."""
        self.books = {}

    def add_book(self, book):
        """Store a book under its isbn."""
        self.books[book.isbn] = book

    def lend(self, isbn):
        """Mark a book as on loan. KeyError if unknown, ValueError if already out."""
        book = self.books[isbn]
        if book.on_loan:
            raise ValueError(f"{book.title} is already on loan")
        book.on_loan = True

    def return_book(self, isbn):
        """Mark a book as returned. KeyError if unknown, ValueError if not on loan."""
        book = self.books[isbn]
        if not book.on_loan:
            raise ValueError(f"{book.title} is not on loan")
        book.on_loan = False

    def available_books(self):
        """Return a list of the books that are not on loan."""
        return [book for book in self.books.values() if not book.on_loan]

    def search(self, text):
        """Return the books whose title or author contains text, ignoring case."""
        needle = text.lower()
        return [
            book
            for book in self.books.values()
            if needle in book.title.lower() or needle in book.author.lower()
        ]

    def save(self, path):
        """Write every book to a JSON file, as a list of dictionaries."""
        records = [book.to_dict() for book in self.books.values()]
        with open(path, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=2)

    @classmethod
    def load(cls, path):
        """Return a Library read from a JSON file made by save.

        A missing file gives an empty Library. ValueError if the file does
        not hold a list (or is not JSON at all).
        """
        library = cls()
        try:
            with open(path, "r", encoding="utf-8") as file:
                records = json.load(file)
        except FileNotFoundError:
            return library
        if type(records) is not list:
            raise ValueError("the library file must hold a list of books")
        for record in records:
            library.add_book(Book.from_dict(record))
        return library
