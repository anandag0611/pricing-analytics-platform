-- 1. Executive KPI Summary
SELECT
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(gross_profit), 2) AS total_gross_profit,
    ROUND((SUM(gross_profit) / SUM(revenue)) * 100, 2) AS gross_margin_percent,
    SUM(quantity_sold) AS total_units_sold,
    ROUND(AVG(discount_percent), 2) AS avg_discount_percent
FROM sales_pricing;


-- 2. Revenue and Profit by Product
SELECT
    product_name,
    category,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(gross_profit), 2) AS total_gross_profit,
    ROUND((SUM(gross_profit) / SUM(revenue)) * 100, 2) AS gross_margin_percent,
    ROUND(AVG(discount_percent), 2) AS avg_discount_percent
FROM sales_pricing
GROUP BY product_name, category
ORDER BY total_gross_profit DESC;


-- 3. Revenue by Region
SELECT
    region,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(gross_profit), 2) AS total_gross_profit,
    SUM(quantity_sold) AS total_units_sold
FROM sales_pricing
GROUP BY region
ORDER BY total_revenue DESC;


-- 4. Discount Leakage Analysis
SELECT
    product_name,
    category,
    ROUND(AVG(discount_percent), 2) AS avg_discount_percent,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(gross_profit), 2) AS total_gross_profit,
    ROUND((SUM(gross_profit) / SUM(revenue)) * 100, 2) AS gross_margin_percent
FROM sales_pricing
GROUP BY product_name, category
HAVING AVG(discount_percent) > 11
ORDER BY avg_discount_percent DESC;