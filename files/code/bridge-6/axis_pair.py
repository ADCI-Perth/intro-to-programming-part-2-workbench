"""Concepts Bridge: the same three values with a truncated and a zero axis."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent

teams = ["Team A", "Team B", "Team C"]
patched = [96, 97, 98]      # per cent of computers patched

fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4))

left.bar(teams, patched)
left.set_ylim(bottom=95)
left.set_title("Axis starts at 95")
left.set_ylabel("Computers patched (%)")

right.bar(teams, patched)
right.set_ylim(bottom=0)
right.set_title("Axis starts at 0")
right.set_ylabel("Computers patched (%)")

fig.tight_layout()
fig.savefig(HERE / "axis_pair.png", dpi=150)
plt.close(fig)
print("Saved axis_pair.png")
