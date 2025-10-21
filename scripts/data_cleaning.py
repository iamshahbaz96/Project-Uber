import pandas as pd
import numpy as np
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

# ──── Fetch data from MySQL ──────────────────────────────
table_data = "data"

data = pd.read_sql(f"SELECT * FROM {table_data}", con=engine)

print("✅ Data fetched from MySQL")

# ─── Paths ────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"