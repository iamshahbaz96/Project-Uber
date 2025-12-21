import pandas as pd
from pathlib import Path
import numpy as np
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
OUTPUT_DIR = BASE_DIR / 'outputs'
SAMPLE_OUTPUT_FILE = 'sample.csv' # Variable only for testing

# ──── Ask if user wants to copy the data to MySQL ─────────
choice = input("Do you want to re-import the CSV into MySQL? (yes/no): ").strip().lower()

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


Dataset = input('Do you want to use CSV file or MySQL table? (MySQL/CSV)').strip().lower()
if Dataset == 'mysql':
    # ──── Use the data from MySQL Database ─────────────────────
    df = pd.read_sql(f"SELECT * FROM {table_data}", con=engine)
    print("✅ Data fetched from MySQL")
else:
    # ──── Use the data directly using pandas ───────────────────
    data = 'ncr_ride_bookings.csv'
    df = pd.read_csv(DATA_DIR / data)
    print("✅ Data fetched from CSV")

# ─── Data Cleaning and Transformation ──────────────────────

#print(df.columns)

# ['Date', 'Time', 'Booking ID', 'Booking Status', 'Customer ID',
#        'Vehicle Type', 'Pickup Location', 'Drop Location', 'Avg VTAT',
#        'Avg CTAT', 'Cancelled Rides by Customer',
#        'Reason for cancelling by Customer', 'Cancelled Rides by Driver',
#        'Driver Cancellation Reason', 'Incomplete Rides',
#        'Incomplete Rides Reason', 'Booking Value', 'Ride Distance',
#        'Driver Ratings', 'Customer Rating', 'Payment Method']

# Create Column for Ride Status including complete, incomplete, cancelled and No ride
ride_conditions = [
    df["Cancelled Rides by Customer"] == 1,
    df["Cancelled Rides by Driver"] == 1,
    df["Incomplete Rides"] == 1,
    df["Booking Status"] == "No Driver Found"
]

ride_choices = [
    "cancelled by customer",
    "cancelled by driver",
    "Incomplete Rides",
    "No Ride Initiated"
]

df["Cancellation_Status"] = np.select(ride_conditions, ride_choices, default="Ride Completed")

# Create Column for Ride reason including complete, incomplete, cancelled and No ride
ride_canc_conditions = [
    df["Cancelled Rides by Customer"] == 1,
    df["Cancelled Rides by Driver"] == 1,
    df["Incomplete Rides"] == 1,
    df["Booking Status"] == "No Driver Found"
]

ride_canc_choices = [
    df["Reason for cancelling by Customer"],
    df["Driver Cancellation Reason"],
    df["Incomplete Rides Reason"],
    df["Booking Status"]
]

df["Cancellation_Reason"] = np.select(ride_canc_conditions, ride_canc_choices, default="Ride Completed")

cancelled_rides = df[df["Cancellation_Status"].isin(["cancelled by customer", "cancelled by driver"])]

Cancellation_Summary = (
    cancelled_rides
        .groupby(["Cancellation_Status", "Cancellation_Reason"])
        .size()
        .reset_index(name="Count")
)

Cancellation_Summary["Percent"] = (
    Cancellation_Summary["Count"]
    / Cancellation_Summary.groupby("Cancellation_Status")["Count"].transform("sum")
)

#Exporting Summary of Cancellation to Output Folder
Cancellation_Summary.to_csv(OUTPUT_DIR / SAMPLE_OUTPUT_FILE, index=False)