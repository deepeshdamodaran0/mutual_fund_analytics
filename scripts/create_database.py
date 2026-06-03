import pandas as pd
import sqlite3

# Connect to SQLite
conn = sqlite3.connect("../data/db/bluestock_mf.db")

# Load datasets
fund = pd.read_csv("../data/raw/01_fund_master.csv")
nav = pd.read_csv("../data/processed/02_nav_history_clean.csv")
perf = pd.read_csv("../data/processed/07_scheme_performance_clean.csv")
txn = pd.read_csv("../data/processed/08_investor_transactions_clean.csv")
aum = pd.read_csv("../data/raw/03_aum_by_fund_house.csv")

# Dimension tables
fund.to_sql("dim_fund", conn, if_exists="replace", index=False)

# Date dimension from NAV data
date_dim = pd.DataFrame()
date_dim["date"] = pd.to_datetime(nav["date"]).drop_duplicates()
date_dim["year"] = date_dim["date"].dt.year
date_dim["month"] = date_dim["date"].dt.month
date_dim["day"] = date_dim["date"].dt.day

date_dim.to_sql(
    "dim_date",
    conn,
    if_exists="replace",
    index=False
)

# Fact tables
nav.to_sql(
    "fact_nav",
    conn,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "fact_transactions",
    conn,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    conn,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database created successfully")