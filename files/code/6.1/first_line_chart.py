"""Section 6.1: a first line chart from a small hand-made list."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")   # draw into a file only, so no window opens
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
tickets = [12, 15, 9, 20, 14]

fig, ax = plt.subplots()
ax.plot(days, tickets, marker="o")
ax.set_title("Help desk tickets this week")
ax.set_xlabel("Day of the week")
ax.set_ylabel("Tickets opened (count)")

fig.savefig(HERE / "first_line_chart.png", dpi=150)
plt.close(fig)
print("Saved first_line_chart.png")
