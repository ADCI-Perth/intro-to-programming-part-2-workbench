"""Section 1.2: string methods."""

raw = "   Jack Wilson  \n"
print(len(raw), len(raw.strip()), raw.strip())
print("  PERTH \n".strip().lower())
print("09/11/2026".replace("/", "-"))

line = "2026-11-09 07:13:45 LOGIN user01"
parts = line.split()
print(parts, len(parts), parts[3])
print("Perth,Notebook,12,6.50".split(","))
print("07:13:45".split(":")[0])

words = ["server", "room", "door"]
print(" ".join(words), "-".join(words), ",".join(words), "".join(words))

filename = "report_2026.csv"
print(filename.endswith(".csv"), filename.startswith("report"), filename.endswith(".txt"))

email = "olivia@example.com"
at = email.find("@")
print(at, email[:at], email[at + 1:], email.find("#"))

sentence = "the report said the backups finished"
print("203.0.113.45".count("."), sentence.count("the"), sentence.count("e"))

print("Perth".isalpha(), "Perth 6000".isalpha(), "6000".isdigit(),
      "60.5".isdigit(), "-5".isdigit(), "".isdigit())
