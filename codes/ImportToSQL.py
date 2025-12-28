import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

# ──── MySQL connection details ────────────────────────────
username = "shahbaz"          # your MySQL username
password = "9960180596"       # your MySQL password
host = "localhost"            # or IP like "127.0.0.1"
port = 3306                   # default MySQL port
database = "uber"             # your database name

# ──── Create SQLAlchemy engine ────────────────────────────
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# ─── Paths ────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'
OUTPUT_DIR = BASE_DIR / 'output'

# Example CSV file path (you can loop if multiple files)
df = "cleaned_data.csv"   # change to your filename
table_data = "cleaned_data" # change to your table name

# Read CSV file
df_data = pd.read_csv(OUTPUT_DIR / df)

# Write DataFrame to MySQL (creates a new table if not exists)
df_data.to_sql(table_data, con=engine, if_exists="replace", index=False)

print("✅ DataFrame successfully imported into MySQL!")