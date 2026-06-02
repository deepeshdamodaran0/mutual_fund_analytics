# Mutual Fund Analytics Project

## Overview

This project is part of the Bluestock Mutual Fund Analytics Capstone Internship.

The objective is to build a complete mutual fund analytics solution including:

* Data ingestion and validation
* ETL pipeline development
* SQLite database integration
* Exploratory Data Analysis (EDA)
* Performance analytics
* Interactive dashboarding
* Advanced analytics and recommendations

---

## Project Structure

```text
mutual_fund_analytics/
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
├── notebooks/
├── scripts/
├── sql/
├── dashboard/
├── reports/
├── data_ingestion.py
├── live_nav_fetch.py
├── requirements.txt
└── README.md
```

---

## Datasets

The project uses mutual fund datasets including:

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

## Features Implemented

### Day 1

* Project structure creation
* GitHub repository setup
* Dependency installation
* CSV data ingestion
* Dataset validation
* Fund master exploration
* AMFI code validation
* Live NAV fetching from mfapi.in

---

## Technologies Used

* Python
* Pandas
* NumPy
* SQLAlchemy
* SQLite
* Matplotlib
* Seaborn
* Plotly
* Jupyter Notebook
* Git & GitHub

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run data ingestion:

```bash
python data_ingestion.py
```

Fetch latest NAV data:

```bash
python live_nav_fetch.py
```

---

## Author

Deepesh Damodaran



