import pandas as pd

# -------------------------
# INVESTOR TRANSACTIONS
# -------------------------

txn = pd.read_csv("../data/raw/08_investor_transactions.csv")

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
)

txn["transaction_type"] = txn["transaction_type"].replace({
    "SIP": "SIP",
    "Sip": "SIP",
    "sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
})

txn = txn[txn["amount_inr"] > 0]

print("\nTransaction Types:")
print(txn["transaction_type"].unique())

print("\nKYC Status:")
print(txn["kyc_status"].unique())

txn.to_csv(
    "../data/processed/08_investor_transactions_clean.csv",
    index=False
)

# -------------------------
# SCHEME PERFORMANCE
# -------------------------

perf = pd.read_csv(
    "../data/raw/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

anomalies = perf[
    (perf["expense_ratio_pct"] < 0.1)
    |
    (perf["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:")
print(len(anomalies))

perf.to_csv(
    "../data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("\nCleaning completed successfully")