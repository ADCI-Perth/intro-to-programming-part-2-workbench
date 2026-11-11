"""Section 6.3: a chart that answers a question (tiny hand-made data)."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent

# Question: which month had the most help desk tickets closed, and which
# team closed the most?
df = pd.DataFrame({
    "month":  ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar", "Mar", "Feb"],
    "team":   ["Network", "Desk", "Network", "Desk", "Network", "Desk", "Desk", "Desk"],
    "closed": [20, 35, 25, 30, None, 50, 20, 5],
})
print("Rows:", len(df))
print("Missing closed:", df["closed"].isna().sum())

# Clean: drop the row with no number, and say so.
clean = df.dropna(subset=["closed"]).copy()
print("Rows after cleaning:", len(clean))

# Summarise.
by_month = clean.groupby("month")["closed"].sum()
by_month = by_month.reindex(["Jan", "Feb", "Mar"])     # calendar order
print(by_month)

# Plot.
fig, ax = plt.subplots()
ax.bar(by_month.index, by_month.values)
ax.set_title("Tickets closed per month")
ax.set_xlabel("Month (2026)")
ax.set_ylabel("Tickets closed (count)")
fig.tight_layout()
fig.savefig(HERE / "tickets_per_month.png", dpi=150)
plt.close(fig)

# One sentence about the chart.
best = by_month.idxmax()
print(f"Sentence: {best} had the most closed tickets, with {int(by_month[best])}.")
