"""Week 4 Concepts Bridge: time three ways of adding up a million numbers."""

import time

import numpy as np

numbers_list = list(range(1_000_000))
numbers_array = np.arange(1_000_000)

# time.perf_counter() gives the time in seconds. Take it before and after
# the job, and subtract, to see how long the job took.
start = time.perf_counter()
total = 0
for number in numbers_list:
    total = total + number
loop_seconds = time.perf_counter() - start

start = time.perf_counter()
total_builtin = sum(numbers_list)
builtin_seconds = time.perf_counter() - start

start = time.perf_counter()
total_numpy = np.sum(numbers_array)
numpy_seconds = time.perf_counter() - start

print("Totals:", total, total_builtin, total_numpy)
print(f"for loop: {loop_seconds:.4f} seconds")
print(f"sum():    {builtin_seconds:.4f} seconds")
print(f"np.sum(): {numpy_seconds:.4f} seconds")
