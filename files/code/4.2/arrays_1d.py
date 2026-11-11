"""Section 4.2: one-dimensional NumPy arrays."""

import numpy as np

# Logins per day for one user over one week (Monday to Sunday).
logins = np.array([4, 5, 5, 4, 9, 3, 12])

print(logins)
print(type(logins))
print("shape:", logins.shape)
print("ndim:", logins.ndim)
print("dtype:", logins.dtype)

# Vectorised arithmetic: one line works on every item.
print(logins * 2)
print(logins + 10)
print(logins / 2)

weekend_extra = np.array([0, 0, 0, 0, 0, 2, 2])
print(logins + weekend_extra)

# Indexing and slicing work like a list.
print(logins[0])
print(logins[-1])
print(logins[1:4])

# A boolean mask: one True or False for each item.
busy = logins > 5
print(busy)
print(logins[busy])
print(logins[logins > 5])
print("Busy days:", busy.sum())

# Making arrays without typing every value.
print(np.arange(5))
print(np.arange(2, 11, 2))
print(np.zeros(4))
print(np.zeros(4, dtype=int))
