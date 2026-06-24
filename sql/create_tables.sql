DROP TABLE IF EXISTS sales_pricing;

CREATE TABLE sales_pricing (
    order_id INTEGER,
    order_date DATE,
    product_id VARCHAR(20),
    product_name VARCHAR(100),
    category VARCHAR(50),
    region VARCHAR(50),
    customer_segment VARCHAR(50),
    list_price NUMERIC(10,2),
    selling_price NUMERIC(10,2),
    discount_percent NUMERIC(5,2),
    unit_cost NUMERIC(10,2),
    quantity_sold INTEGER,
    revenue NUMERIC(12,2),
    gross_profit NUMERIC(12,2),
    gross_margin_percent NUMERIC(8,2)
);