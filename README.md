# Retail Sales & Financial Performance Analysis

An end-to-end MBA business analytics project that explores retail revenue, costs, profit, product categories, regions, sales channels, and discount patterns through Python, SQL, and an interactive Streamlit dashboard.

> **Data note:** `data/retail_sales.csv` is a synthetic demonstration dataset created for learning and portfolio practice. It does not represent a real company or actual customer transactions. Do not present the sample results as real business findings.

## Project objectives
- Measure revenue, total costs, profit, and profit margin.
- Compare performance across product categories and regions.
- Explore monthly sales trends and online vs. store performance.
- Examine how order-level discounts relate to revenue and profit.
- Present filterable business metrics in an interactive dashboard.

## Tools and technologies
- Python
- Pandas
- Plotly
- Streamlit
- SQL

## Repository structure
```text
retail_sales_financial_analysis/
├── app.py
├── analysis.py
├── requirements.txt
├── data/
│   └── retail_sales.csv
└── sql/
    └── analysis_queries.sql
```

## Run locally
1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Launch the dashboard:

   ```bash
   streamlit run app.py
   ```

6. To print summary analysis in the terminal:

   ```bash
   python analysis.py
   ```

## Dashboard features
- KPI cards for revenue, profit, profit margin, and order count.
- Filters for date range, region, product category, and sales channel.
- Monthly revenue and profit trend.
- Category-wise and region-wise performance.
- Online vs. store revenue comparison.
- Download filtered transaction data as CSV.

## Business questions explored
1. Which product categories contribute the most revenue?
2. Which regions generate the highest sales and profit?
3. How do online and physical store channels compare?
4. How does profit margin vary across filtered transactions?
5. What patterns appear across discount levels?

## Important interpretation note
The project supports descriptive analysis. A relationship between discount levels and profit does not, by itself, prove that discounts caused a change in profit. Business decisions should also consider seasonality, product mix, customer behaviour, and operating costs.

## Future improvements
- Connect a real, properly licensed retail dataset.
- Add customer-level segmentation and cohort analysis.
- Add forecasting with a time-series model.
- Build a Power BI version of the dashboard.
- Add automated data-quality checks and unit tests.

## Author
Sunny Rohra  
MBA | Finance | Business Analytics
