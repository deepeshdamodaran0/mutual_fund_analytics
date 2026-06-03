import pandas as pd

# Investor Transactions
df1 = pd.read_csv("C:\\Users\\deepe\\bluestock_internship\\mutual_fund_analytics\\data\\raw\\08_investor_transactions.csv")

print("=== INVESTOR TRANSACTIONS ===")
print(df1.columns)
print(df1.dtypes)
print(df1.head())

print("\n" + "="*60 + "\n")

# Scheme Performance
df2 = pd.read_csv("C:\\Users\\deepe\\bluestock_internship\\mutual_fund_analytics\\data\\raw\\07_scheme_performance.csv")

print("=== SCHEME PERFORMANCE ===")
print(df2.columns)
print(df2.dtypes)
print(df2.head())