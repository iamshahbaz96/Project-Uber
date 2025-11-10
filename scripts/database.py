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

# ──── Ask if user wants to re-import ──────────────────────
choice = input("Do you want to re-import the CSV into MySQL? (yes/no): ").strip().lower()


# ─── Paths ────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

if choice == "yes":
    # Example CSV file path (you can loop if multiple files)
    data = "ncr_ride_bookings.csv"   # change to your filename
    table_data = "data" # change to your table name

    # Read CSV file
    df_data = pd.read_csv(DATA_DIR / data)

    # Write DataFrame to MySQL (creates a new table if not exists)
    df_data.to_sql(table_data, con=engine, if_exists="replace", index=False)

    print("✅ DataFrame successfully imported into MySQL!")

else:
    print("⚡ Skipped importing, using existing data in MySQL")