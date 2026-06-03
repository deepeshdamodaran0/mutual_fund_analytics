-- Total Funds
SELECT COUNT(*) AS total_funds
FROM dim_fund;

-- Average NAV
SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- Top 5 Funds by AUM
SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- Transaction Summary
SELECT transaction_type,
       COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY transaction_type;

-- Average 3-Year Return
SELECT AVG(return_3yr_pct)
FROM fact_performance;