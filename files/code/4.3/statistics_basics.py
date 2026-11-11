"""Section 4.3: basic statistics with NumPy."""

import numpy as np

# Response times in milliseconds for eight requests to a web page.
times = np.array([20, 22, 19, 21, 20, 23, 95, 20])

print("sum:   ", times.sum())
print("mean:  ", times.mean())
print("median:", np.median(times))
print("min:   ", times.min())
print("max:   ", times.max())
print("argmax:", times.argmax())

# The standard deviation by hand, then with NumPy.
values = np.array([2, 4, 4, 6])
mean = values.mean()
differences = values - mean
squares = differences ** 2
print("mean:", mean)
print("differences:", differences)
print("squares:", squares)
print("mean of squares:", squares.mean())
print("square root:", squares.mean() ** 0.5)
print("np.std:", values.std())

# axis=0 and axis=1 on a table.
# Rows are days. Columns are users.
table = np.array([
    [4, 8, 1, 6],
    [5, 5, 3, 9],
    [5, 5, 2, 7],
])
print("whole table:", table.sum())
print("axis=0 (down each column, one answer per user):", table.sum(axis=0))
print("axis=1 (along each row, one answer per day):  ", table.sum(axis=1))
print("mean per user:", table.mean(axis=0))
print("max per day:", table.max(axis=1))
print("busiest day position:", table.sum(axis=1).argmax())
