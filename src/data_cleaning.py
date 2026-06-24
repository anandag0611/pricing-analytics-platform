import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

raw_file = os.path.join(
    base_dir,
    "data",
    "raw",
    "sales_pricing_raw.csv"
)

processed_folder = os.path.join(
    base_dir,
    "data",
    "processed"
)

os.makedirs(processed_folder, exist_ok=True)

processed_file = os.path.join(
    processed_folder,
    "sales_pricing_clean.csv"
)

df = pd.read_csv(raw_file)

print("Rows Before Cleaning:", len(df))

df = df.drop_duplicates()

df = df[df["quantity_sold"] > 0]
df = df[df["selling_price"] > 0]
df = df[df["revenue"] > 0]

df["order_date"] = pd.to_datetime(df["order_date"])

df["gross_margin_percent"] = (
    df["gross_profit"] / df["revenue"]
) * 100

df["gross_margin_percent"] = (
    df["gross_margin_percent"]
    .round(2)
)

df.to_csv(processed_file, index=False)

print("Rows After Cleaning:", len(df))
print("Cleaned file created successfully!")
print(f"Saved to: {processed_file}")