"""Section 5.4: a mean skips missing values without telling you."""

import pandas as pd

scores = pd.Series([10, None, 30])
print(scores)
print(scores.mean())
print(scores.fillna(0).mean())
print(len(scores), scores.count())
