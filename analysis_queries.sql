-- Retail Sales & Financial Performance Analysis
-- Run these queries after importing data/retail_sales.csv into a SQL table named retail_sales.

-- 1. Overall business performance
SELECT
    SUM(revenue) AS total_revenue,
    SUM(cost + shipping_cost) AS total_cost,
    SUM(profit) AS total_profit,
    ROUND(100.0 * SUM(profit) / NULLIF(SUM(revenue), 0), 2) AS profit_margin_pct
FROM retail_sales;

-- 2. Monthly revenue and profit trend
SELECT
    DATE_TRUNC('month', CAST(order_date AS DATE)) AS sales_month,
    SUM(revenue) AS revenue,
    SUM(profit) AS profit
FROM retail_sales
GROUP BY 1
ORDER BY 1;

-- 3. Category-wise profitability
SELECT
    category,
    SUM(revenue) AS revenue,
    SUM(profit) AS profit,
    ROUND(100.0 * SUM(profit) / NULLIF(SUM(revenue), 0), 2) AS profit_margin_pct
FROM retail_sales
GROUP BY category
ORDER BY profit DESC;

-- 4. Region-wise performance
SELECT region, COUNT(DISTINCT order_id) AS orders,
       SUM(revenue) AS revenue, SUM(profit) AS profit
FROM retail_sales
GROUP BY region
ORDER BY revenue DESC;

-- 5. Sales channel comparison
SELECT sales_channel, SUM(revenue) AS revenue, SUM(profit) AS profit,
       COUNT(DISTINCT order_id) AS orders
FROM retail_sales
GROUP BY sales_channel
ORDER BY revenue DESC;

-- 6. Discount impact (descriptive comparison, not causal proof)
SELECT discount_pct, COUNT(*) AS order_lines,
       AVG(revenue) AS average_revenue,
       AVG(profit) AS average_profit
FROM retail_sales
GROUP BY discount_pct
ORDER BY discount_pct;
