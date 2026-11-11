"""Section 4.3: z-scores, and how one extreme value changes the statistics."""

import numpy as np

# Megabytes downloaded by one account on each of ten days.
downloads = np.array([50, 52, 48, 51, 49, 50, 53, 47, 50, 120])

mean = downloads.mean()
std = downloads.std()
print(f"mean = {mean:.1f}, std = {std:.2f}")

# Vectorised: one line gives a z-score for every day.
z = (downloads - mean) / std
print(np.round(z, 2))

# Which days are more than 2.5 standard deviations from the mean?
mask = np.abs(z) > 2.5
print(mask)
print("Flagged values:", downloads[mask])

# The extreme value pulls the mean and the standard deviation.
normal_days = downloads[:-1]
print(f"Without the last day: mean = {normal_days.mean():.1f}, "
      f"std = {normal_days.std():.2f}")
print(f"Median with the last day:    {np.median(downloads)}")
print(f"Median without the last day: {np.median(normal_days)}")
