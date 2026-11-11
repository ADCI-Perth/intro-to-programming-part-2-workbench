"""Section 1.2: f-string format specs and a neat table."""

price = 6.5
total = 1234567.891
print(f"{price:.2f}")
print(f"{total:.1f}")
print(f"{total:,}")
print(f"{total:,.2f}")

word = "abc"
print(f"[{word:>8}]")
print(f"[{word:<8}]")
print(f"[{42:>8}]")
print(f"[{3.14159:>8.2f}]")

rows = [
    ("Notebook", 120, 6.5),
    ("Pen pack", 85, 4.0),
    ("Desk lamp", 9, 32.0),
]

print(f"{'Product':<10}{'Units':>8}{'Price':>8}")
print("-" * 26)
for product, units, price in rows:
    print(f"{product:<10}{units:>8}{price:>8.2f}")
