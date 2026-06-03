import pandas as pd

nav = pd.read_csv("../data/raw/02_nav_history.csv")

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Sort data
nav = nav.sort_values(
    by=["amfi_code", "date"]
)

# Remove duplicates (safety)
nav = nav.drop_duplicates()

# Keep only valid NAVs
nav = nav[nav["nav"] > 0]

# Forward fill NAV within each scheme
nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
       .ffill()
)

# Save cleaned data
nav.to_csv(
    "../data/processed/02_nav_history_clean.csv",
    index=False
)

print("NAV cleaning completed")
print(nav.shape)