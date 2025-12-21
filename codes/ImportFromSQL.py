import pandas as pd
from sqlalchemy import create_engine

# ──── MySQL connection details ────────────────────────────
username = "shahbaz"          # your MySQL username
password = "9960180596"       # your MySQL password
host = "localhost"            # or IP like "127.0.0.1"
port = 3306                   # default MySQL port
database = "uber"             # your database name

# ──── Create SQLAlchemy engine ────────────────────────────
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

table_name = "data" # change to your table name

df = pd.read_sql(f"SELECT * FROM {table_name}", con=engine)

print("✅ DataFrame successfully imported from MySQL!")

print(df)