import pandas as pd
import os
from sqlalchemy import create_engine

# -------------------
# PostgreSQL Settings
# -------------------

DB_USER = "postgres"
DB_PASSWORD = "Venky$1234"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "pricing_analytics"

# -------------------
# Build Connection
# -------------------

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# -------------------
# Locate CSV File
# -------------------

base_dir = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

csv_file = os.path.join(
    base_dir,
    "data",
    "processed",
    "sales_pricing_clean.csv"
)

# -------------------
# Load Data
# -------------------

df = pd.read_csv(csv_file)

print(f"Rows Found: {len(df)}")

df.to_sql(
    "sales_pricing",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully!")