# Mutual Fund Analytics Platform

## Overview

The Mutual Fund Analytics Platform is a comprehensive financial analytics project developed during the Data Analytics Internship at Bluestock Fintech.

The project aims to analyze mutual fund performance, investor behavior, SIP trends, portfolio concentration, and risk metrics using Python, SQL, SQLite, and Power BI.

The platform combines data engineering, exploratory data analysis, financial analytics, business intelligence, and advanced risk modeling to provide actionable insights for investors and financial institutions.

---

## Project Objectives

* Build a complete mutual fund analytics solution.
* Develop an end-to-end data analytics pipeline.
* Perform financial performance analysis.
* Analyze investor behavior and SIP trends.
* Create interactive Power BI dashboards.
* Develop a simple fund recommendation system.
* Generate business insights through advanced analytics.

---

## Project Structure

```text
mutual_fund_analytics/
├── dashboard/
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
├── notebooks/
├── reports/
├── scripts/
├── sql/
├── README.md
├── requirements.txt
```

---

## Datasets Used

The project utilizes multiple mutual fund datasets:

* Fund Master
* NAV History
* AUM by Fund House
* Monthly SIP Inflows
* Category Inflows
* Industry Folio Count
* Scheme Performance
* Investor Transactions
* Portfolio Holdings
* Benchmark Indices

---

## Project Phases

### Phase 1: Data Ingestion & Validation

* CSV Data Ingestion
* Data Validation
* AMFI Code Validation
* Live NAV Fetching
* SQLite Database Integration

### Phase 2: Data Cleaning & Preprocessing

* Missing Value Handling
* Duplicate Removal
* Data Type Conversion
* Date Standardization
* Feature Engineering

### Phase 3: Exploratory Data Analysis (EDA)

* AUM Analysis
* SIP Trend Analysis
* Category Inflow Analysis
* Industry Folio Analysis
* Investor Demographic Analysis
* Geographic Analysis

### Phase 4: Performance Analytics

* CAGR Calculation
* Sharpe Ratio Analysis
* Sortino Ratio Analysis
* Alpha & Beta Analysis
* Maximum Drawdown Analysis
* Fund Scorecard Development
* Benchmark Comparison

### Phase 5: Advanced Analytics

* Value at Risk (VaR)
* Conditional Value at Risk (CVaR)
* Rolling 90-Day Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Fund Recommendation System
* Sector HHI Concentration Analysis

### Phase 6: Business Intelligence Dashboard

A four-page Power BI dashboard was developed covering:

1. Mutual Fund Industry Overview
2. Fund Performance Analytics
3. Investor Analytics
4. SIP and Market Trends

---

## Key Results

### Top Fund by Composite Score

* Mirae Asset Tax Saver Fund – Score: 100

### Highest Alpha Fund

* SBI Small Cap Fund – Alpha: 0.303

### Highest Sharpe Ratio (Low Risk Category)

* ICICI Prudential Liquid Fund – Sharpe Ratio: 7.68

### Investor Cohort Analysis

* 2024 Cohort invested over ₹349 Crore

### SIP Continuity Analysis

* 2,762 investors classified as At Risk
* 188 investors classified as Healthy

### Portfolio Concentration Analysis

* Axis Bluechip Fund recorded the highest HHI concentration score

---

## Technologies Used

### Programming & Analytics

* Python
* Pandas
* NumPy

### Database

* SQLite
* SQLAlchemy
* SQL

### Visualization

* Power BI
* Matplotlib
* Plotly

### Development Tools

* Jupyter Notebook
* Git
* GitHub

---

## Deliverables

* Final_Report.pdf
* Advanced_Analytics.ipynb
* recommender.py
* var_cvar_report.csv
* rolling_sharpe_chart.png
* Power BI Dashboard (.pbix)
* Project Presentation (.pptx)

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Data Ingestion

```bash
python data_ingestion.py
```

### Fetch Latest NAV Data

```bash
python live_nav_fetch.py
```

### Run Fund Recommender

```bash
python recommender.py
```

---

## Future Enhancements

* Real-time NAV Integration
* Machine Learning-Based Fund Recommendation
* Investor Churn Prediction
* Portfolio Optimization Engine
* Web-Based Analytics Portal
* Mobile Dashboard Integration

---

## Author

Deepesh A

M.Sc. Computer Science

Mangalore University (2025)

Data Analytics Intern – Bluestock Fintech
