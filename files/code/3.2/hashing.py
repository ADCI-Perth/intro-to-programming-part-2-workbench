"""Section 3.2: hashing text and files with hashlib (SHA-256)."""

import hashlib
from pathlib import Path


def text_hash(text):
    """Return the SHA-256 hash of a string, as 64 hexadecimal characters."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def file_hash(path):
    """Return the SHA-256 hash of a file, read in binary mode."""
    with open(path, "rb") as file:
        data = file.read()
    return hashlib.sha256(data).hexdigest()


def file_hash_in_chunks(path):
    """The same answer as file_hash, but reads a large file a piece at a time."""
    hasher = hashlib.sha256()
    with open(path, "rb") as file:
        chunk = file.read(4096)
        while chunk != b"":
            hasher.update(chunk)
            chunk = file.read(4096)
    return hasher.hexdigest()


print("--- hashing text ---")
digest = text_hash("hello")
print(digest)
print(len(digest))

print("--- same input, same hash ---")
print(text_hash("hello") == text_hash("hello"))

print("--- a tiny change gives a very different hash ---")
print(text_hash("Pay Jack $100"))
print(text_hash("Pay Jack $900"))

print("--- any length in, 64 characters out ---")
print(len(text_hash("a")))
print(len(text_hash("a" * 100000)))

print("--- hashing a file ---")
# A small demo file, saved next to this program.
demo = Path(__file__).with_name("demo_note.txt")
with open(demo, "wb") as file:
    file.write("hello".encode("utf-8"))

print(file_hash(demo))
print(file_hash(demo) == text_hash("hello"))
print(file_hash_in_chunks(demo) == file_hash(demo))

print("--- checking a file against a published hash ---")
published = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
if file_hash(demo) == published:
    print("The file matches the published hash.")
else:
    print("Warning: the file does NOT match. Do not use it.")

# Tidy up: delete the demo file.
demo.unlink()
