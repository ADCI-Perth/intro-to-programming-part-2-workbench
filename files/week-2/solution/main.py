"""Text menu for the library-loan manager (Week 2 model solution).

Books are loaded from library.json when the program starts, and saved to
it when the user chooses Quit.
"""

from pathlib import Path

from library import Book, Library

# library.json sits next to this file.
LIBRARY_FILE = Path(__file__).parent / "library.json"

MENU = """
1. Add a book
2. List available books
3. Lend a book
4. Return a book
5. Search
6. Quit
"""


def add_book(library):
    """Ask for a book's details and add it. Empty fields are refused."""
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    isbn = input("ISBN: ").strip()
    if not title or not author or not isbn:
        print("Title, author and ISBN cannot be empty.")
        return
    library.add_book(Book(title, author, isbn))
    print("Book added.")


def list_available(library):
    """Print every book that is not on loan."""
    books = library.available_books()
    if not books:
        print("No books available.")
    for book in books:
        print(book)


def lend_book(library):
    """Lend a book by its isbn, with friendly messages for mistakes."""
    isbn = input("ISBN to lend: ").strip()
    try:
        library.lend(isbn)
        print("Lent.")
    except KeyError:
        print("No book with that ISBN.")
    except ValueError as error:
        print(error)


def return_book(library):
    """Return a book by its isbn, with friendly messages for mistakes."""
    isbn = input("ISBN to return: ").strip()
    try:
        library.return_book(isbn)
        print("Returned.")
    except KeyError:
        print("No book with that ISBN.")
    except ValueError as error:
        print(error)


def search_books(library):
    """Ask for text and print the books whose title or author matches."""
    text = input("Search for: ").strip()
    results = library.search(text)
    if not results:
        print("No matches.")
    for book in results:
        print(book)


def main():
    """Load the books, show the menu until Quit, then save the books."""
    try:
        library = Library.load(LIBRARY_FILE)
    except (ValueError, KeyError, TypeError):
        # The file is there, but it is damaged or is not a library file.
        # Stop here, so that Quit does not write over it.
        print("Could not read library.json. Fix or delete the file, then run again.")
        return
    print(f"Books loaded: {len(library.books)}")
    while True:
        print(MENU)
        try:
            choice = input("Choose 1-6: ").strip()
        except EOFError:
            choice = "6"
        if choice == "1":
            add_book(library)
        elif choice == "2":
            list_available(library)
        elif choice == "3":
            lend_book(library)
        elif choice == "4":
            return_book(library)
        elif choice == "5":
            search_books(library)
        elif choice == "6":
            library.save(LIBRARY_FILE)
            print("Goodbye. Books saved.")
            break
        else:
            print("Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
