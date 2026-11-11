"""Section 6.3: the same clean data, a second question (which team?)."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent

df = pd.DataFrame({
    "month":  ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar", "Mar", "Feb"],
    "team":   ["Network", "Desk", "Network", "Desk", "Network", "Desk", "Desk", "Desk"],
    "closed": [20, 35, 25, 30, None, 50, 20, 5],
})
clean = df.dropna(subset=["closed"])
by_team = clean.groupby("team")["closed"].sum().sort_values(ascending=False)
print(by_team)

fig, ax = plt.subplots()
ax.bar(by_team.index, by_team.values)
ax.set_title("Tickets closed per team, January to March")
ax.set_xlabel("Team")
ax.set_ylabel("Tickets closed (count)")
fig.tight_layout()
fig.savefig(HERE / "tickets_per_team.png", dpi=150)
plt.close(fig)
