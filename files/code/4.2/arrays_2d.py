"""Section 4.2: two-dimensional NumPy arrays (a table of numbers)."""

import numpy as np

# Rows are days (Monday, Tuesday, Wednesday).
# Columns are users (user01, user02, user03, user04).
table = np.array([
    [4, 8, 1, 6],
    [5, 5, 3, 9],
    [5, 5, 2, 7],
])

print(table)
print("shape:", table.shape)
print("ndim:", table.ndim)

# One cell: table[row, col]
print(table[0, 1])
print(table[2, 3])

# One whole row, and one whole column.
print(table[1])
print(table[:, 0])
print(table[:, -1])

# A smaller table: the first two rows and the last two columns.
print(table[0:2, 2:4])

# Arithmetic and masks work on every cell.
print(table * 10)
print(table > 5)
print(table[table > 5])

# zeros with a shape gives an empty table to fill in.
blank = np.zeros((2, 3), dtype=int)
blank[0, 1] = 7
print(blank)
