"""Section 5.1: a first DataFrame, made by hand."""

import pandas as pd

data = {
    "user": ["user01", "user02", "user03"],
    "logins": [12, 7, 30],
    "failed": [0, 2, 9],
}
df = pd.DataFrame(data)

print(df)
print(df.shape)

logins = df["logins"]
print(logins)
print(type(logins))
print(logins.sum())
