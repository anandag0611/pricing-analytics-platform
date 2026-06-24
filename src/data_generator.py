import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

np.random.seed(42)

products = [
    ("P001", "Laptop Basic", "Electronics", 700, 480),
    ("P002", "Laptop Pro", "Electronics", 1200, 850),
    ("P003", "Wireless Mouse", "Accessories", 40, 18),
    ("P004", "Keyboard", "Accessories", 65, 30),
    ("P005", "Office Chair", "Furniture", 250, 140),
    ("P006", "Standing Desk", "Furniture", 600, 390),
    ("P007", "Monitor 24 inch", "Electronics", 180, 110),
    ("P008", "Monitor 32 inch", "Electronics", 350, 230),
    ("P009", "Headset", "Accessories", 90, 45),
    ("P010", "Webcam", "Accessories", 120, 70),
]

regions = ["North", "South", "East", "West"]
segments = ["Consumer", "Small Business", "Enterprise"]

rows = []

start_date = datetime(2024, 1, 1)

for i in range(5000):

    product = random.choice(products)

    product_id = product[0]
    product_name = product[1]
    category = product[2]
    list_price = product[3]
    unit_cost = product[4]

    order_date = start_date + timedelta(days=random.randint(0, 364))

    region = random.choice(regions)
    customer_segment = random.choice(segments)

    discount_percent = np.random.choice(
        [0, 5, 10, 15, 20, 25, 30],
        p=[0.15, 0.20, 0.25, 0.15, 0.12, 0.08, 0.05]
    )

    selling_price = list_price * (1 - discount_percent / 100)

    quantity_sold = max(1, int(np.random.normal(8, 3)))

    revenue = selling_price * quantity_sold

    gross_profit = (selling_price - unit_cost) * quantity_sold

    gross_margin_percent = (
        gross_profit / revenue * 100
    ) if revenue != 0 else 0

    rows.append([
        i + 1,
        order_date.date(),
        product_id,
        product_name,
        category,
        region,
        customer_segment,
        list_price,
        round(selling_price, 2),
        discount_percent,
        unit_cost,
        quantity_sold,
        round(revenue, 2),
        round(gross_profit, 2),
        round(gross_margin_percent, 2)
    ])

columns = [
    "order_id",
    "order_date",
    "product_id",
    "product_name",
    "category",
    "region",
    "customer_segment",
    "list_price",
    "selling_price",
    "discount_percent",
    "unit_cost",
    "quantity_sold",
    "revenue",
    "gross_profit",
    "gross_margin_percent"
]

df = pd.DataFrame(rows, columns=columns)

os.makedirs("data/raw", exist_ok=True)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

raw_folder = os.path.join(base_dir, "data", "raw")

output_path = os.path.join(raw_folder, "sales_pricing_raw.csv")

df.to_csv(output_path, index=False)

print(f"File saved to: {output_path}")

print("Dataset Created Successfully!")
print(df.head())
print(f"Rows Generated: {len(df)}")