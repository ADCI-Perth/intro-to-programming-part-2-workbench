"""Section 1.3: ASCII and UTF-8."""

print(ord("A"), ord("a"), ord("0"), ord(" "), chr(65), chr(97))
print(ord("é"), ord("€"), "cafe".isascii(), "café".isascii())

data = "café".encode("utf-8")
print(data, type(data), list(data))
print(b"caf\xc3\xa9".decode("utf-8"))

print(len("café"), len("café".encode("utf-8")))
print(len("€".encode("utf-8")), len("😀".encode("utf-8")))

wrong = data.decode("latin-1")
print(wrong, len(wrong))
print(wrong.encode("latin-1").decode("utf-8"))

try:
    "café".encode("ascii")
except UnicodeEncodeError as error:
    print("UnicodeEncodeError:", error)
