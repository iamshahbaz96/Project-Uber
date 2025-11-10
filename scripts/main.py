import pandas as pd
from pathlib import Path

# ─── Paths ────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'

data = 'ncr_ride_bookings.csv'

df = pd.read_csv(DATA_DIR / data)

# Quick overview
print(df.shape)
print(df.info())
print(df.describe(include='all').T)