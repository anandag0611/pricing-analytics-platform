# End-to-End Pricing Analytics & Revenue Optimization Platform
![Dashboard Preview](dashboard/powerbi_screenshots/page1_executive_summary.png)

## Project Overview

This project is an end-to-end Pricing Analytics solution built using Python, PostgreSQL, SQL, Power BI, and DAX.

The objective is to analyze product pricing, discounts, profitability, and revenue performance to identify pricing optimization opportunities and support business decision-making.

---

## Business Problem

Organizations often struggle to understand:

* Which products generate the highest revenue and profit
* How discounts impact profitability
* Which products are candidates for price increases
* Which products require pricing strategy adjustments

This project addresses these challenges through data analysis, SQL reporting, and interactive Power BI dashboards.

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python, Pandas, NumPy |
| Database | PostgreSQL, SQLAlchemy |
| SQL | PostgreSQL SQL |
| Visualization | Power BI, DAX |
| Version Control | Git, GitHub |

---

## Project Architecture

![Project Architecture](diagrams/pricing_analytics_architecture.png)

---

## Project Structure

```text
pricing-analytics-platform/
│
├── dashboard/
│   ├── pricing_analytics_dashboard.pbix
│   └── powerbi_screenshots/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── diagrams/
│   └── pricing_analytics_architecture.png
│
├── reports/
│
├── sql/
│   ├── create_tables.sql
│   └── kpi_queries.sql
│
├── src/
│   ├── data_generator.py
│   ├── data_cleaning.py
│   ├── db_load.py
│   └── pricing_analysis.py
│
├── README.md
└── requirements.txt
```

## Key Features

### Data Engineering

* Generated 5,000+ realistic sales transactions
* Cleaned and transformed raw data using Python
* Loaded processed data into PostgreSQL

### Analytics

* Revenue Analysis
* Profitability Analysis
* Discount Analysis
* Margin Analysis
* Product Performance Evaluation

### Dashboard Reporting

#### Executive KPI Summary

* Total Revenue
* Gross Profit
* Gross Margin %
* Average Discount %
* Units Sold

#### Product Pricing Analysis

* Revenue by Product
* Profit by Product
* Discount Analysis
* Margin Analysis

#### Executive Recommendations

* Pricing optimization opportunities
* Discount reduction opportunities
* Product promotion recommendations
* Rule-based DAX classifications

---

## Dashboard Screenshots

### Executive KPI Summary

![Executive KPI Summary](dashboard/powerbi_screenshots/page1_executive_summary.png)

### Product Pricing Analysis

![Product Pricing Analysis](dashboard/powerbi_screenshots/page2_product_analysis.png)

### Executive Recommendations

![Executive Recommendations](dashboard/powerbi_screenshots/page3_recommendations.png)

---

## Key Results

| KPI              |   Value |
| ---------------- | ------: |
| Revenue          | $11.73M |
| Gross Profit     |  $3.04M |
| Gross Margin     |  25.90% |
| Units Sold       |  37,450 |
| Average Discount |  11.35% |

---

## How to Run

1. Clone the repository.
2. Install the required Python packages.
3. Generate sample sales data.
4. Clean and transform the data.
5. Load the dataset into PostgreSQL.
6. Execute the SQL scripts.
7. Open the Power BI dashboard.

---

## Future Enhancements

- Automated ETL pipeline
- Revenue forecasting
- Price elasticity analysis
- Customer segmentation
- Automated dashboard refresh
