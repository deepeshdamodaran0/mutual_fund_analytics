import pandas as pd
import os

data_path = "data/raw"

files = sorted(
    [f for f in os.listdir(data_path) if f.endswith(".csv")]
)

for file in files:
    print("\n" + "=" * 60)
    print(f"Dataset: {file}")

    df = pd.read_csv(os.path.join(data_path, file))

    print(f"Shape: {df.shape}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())


    import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nFund Houses")
print(df["fund_house"].unique())

print("\nCategories")
print(df["category"].unique())

print("\nSub Categories")
print(df["sub_category"].unique())

print("\nRisk Categories")
print(df["risk_category"].unique())



import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("\nAMFI CODE VALIDATION")
print("Fund Master Codes:", len(fund_codes))
print("NAV History Codes:", len(nav_codes))
print("Missing Codes:", len(missing_codes))

if len(missing_codes) == 0:
    print("All AMFI codes are present in NAV history")
else:
    print("Missing AMFI Codes:")
    print(missing_codes)