# Data Dictionary

## dim_fund

| Column | Type | Description |
|----------|--------|-------------|
| amfi_code | INTEGER | AMFI scheme code |
| fund_house | TEXT | Mutual fund company |
| scheme_name | TEXT | Scheme name |
| category | TEXT | Fund category |
| sub_category | TEXT | Fund sub-category |

## fact_nav

| Column | Type | Description |
|----------|--------|-------------|
| amfi_code | INTEGER | AMFI scheme code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |