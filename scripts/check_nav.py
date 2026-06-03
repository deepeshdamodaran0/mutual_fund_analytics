import pandas as pd

nav = pd.read_csv("../data/raw/02_nav_history.csv")

print("Shape:", nav.shape)

print("\nDuplicate Rows:")
print(nav.duplicated().sum())

print("\nNAV <= 0:")
print((nav["nav"] <= 0).sum())

print("\nMissing NAV:")
print(nav["nav"].isna().sum())