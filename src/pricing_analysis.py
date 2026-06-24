import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_path = os.path.join(
    base_dir,
    "data",
    "processed",
    "sales_pricing_clean.csv"
)

df = pd.read_csv(file_path)

print("\n===== EXECUTIVE KPI SUMMARY =====\n")

total_revenue = df["revenue"].sum()
total_profit = df["gross_profit"].sum()
total_units = df["quantity_sold"].sum()

margin_pct = (
    total_profit / total_revenue
) * 100

avg_discount = df["discount_percent"].mean()

print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Gross Profit: ${total_profit:,.2f}")
print(f"Gross Margin %: {margin_pct:.2f}%")
print(f"Total Units Sold: {total_units:,}")
print(f"Average Discount %: {avg_discount:.2f}%")

print("\n===== TOP PRODUCTS BY REVENUE =====\n")

top_products = (
    df.groupby("product_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)

print("\n===== REVENUE BY CATEGORY =====\n")

category_revenue = (
    df.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print(category_revenue)

print("\n===== REGION PERFORMANCE =====\n")

region_revenue = (
    df.groupby("region")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print(region_revenue)

print("\n===== HIGHEST DISCOUNT PRODUCTS =====\n")

discount_products = (
    df.groupby("product_name")["discount_percent"]
    .mean()
    .sort_values(ascending=False)
)

print(discount_products.head(10))

print("\n===== TOP 5 PRODUCTS BY PROFIT =====\n")

top_profit = (
    df.groupby("product_name")["gross_profit"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print(top_profit)

print("\n===== LOWEST PROFIT PRODUCTS =====\n")

low_profit = (
    df.groupby("product_name")["gross_profit"]
    .sum()
    .sort_values()
    .head(5)
)

print(low_profit)

print("\n===== AVERAGE DISCOUNT BY PRODUCT =====\n")

discounts = (
    df.groupby("product_name")["discount_percent"]
    .mean()
    .sort_values(ascending=False)
)

print(discounts)