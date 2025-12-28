import pandas as pd
from pathlib import Path
import numpy as np


#------------Paths-------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'
OUTPUT_DIR = BASE_DIR / 'output'

data = "ncr_ride_bookings.csv"   # filename

# 1. LOAD DATA

#Read CSV file
df = pd.read_csv(DATA_DIR / data)


# TO READ ALL THE COLUMNS OF THE DATAFRAME
# print(raw.columns)
#[
# 'Date', 'Time', 'Booking ID', 'Booking Status', 'Customer ID',
#    'Vehicle Type', 'Pickup Location', 'Drop Location', 'Avg VTAT',
#    'Avg CTAT', 'Cancelled Rides by Customer',
#    'Reason for cancelling by Customer', 'Cancelled Rides by Driver',
#    'Driver Cancellation Reason', 'Incomplete Rides',
#    'Incomplete Rides Reason', 'Booking Value', 'Ride Distance',
#    'Driver Ratings', 'Customer Rating', 'Payment Method'
#]

# 2. DATA CLEANING

# Convert Date and Time into a single Datetime object for precise analysis
# This allows us to calculate trends across days and hours easily
df['Date'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
df = df.rename(columns={'Date': 'Pickup_DateTime'})

# Remove triple quotes/extra characters often found in CSV ID columns
df['Booking ID'] = df['Booking ID'].astype(str).str.replace('"', '', regex=False)
df['Customer ID'] = df['Customer ID'].astype(str).str.replace('"', '', regex=False)

# REVISE BOOKING STATUS AS PER UNDERSTANDALBE CATEGORIES

status_map = {
    'Cancelled by Customer': 'Ride not booked',
    'Cancelled by Driver': 'Ride not booked',
    'No Driver Found': 'Ride not booked',
    'Incomplete': 'Ride booked but incomplete',
    'Completed': 'Ride complete'
}

df['ride_status'] = df['Booking Status'].map(status_map)

# 3. TIME FEATURING

# Extract basic time parts

df['Day_of_Week'] = df['Pickup_DateTime'].dt.day_name()
df['Month'] = df['Pickup_DateTime'].dt.month_name()
df['Hour'] = df['Pickup_DateTime'].dt.hour

# Define Business Logic for "Time Slots" (Morning Rush, Evening Rush, etc.)
def assign_time_slot(hour):
    if 6 <= hour < 11:
        return 'Morning Rush'
    elif 11 <= hour < 16:
        return 'Afternoon'
    elif 16 <= hour < 21:
        return 'Evening Rush'
    else:
        return 'Late Night'

df['Time_Slot'] = df['Hour'].apply(assign_time_slot)

# 4. HANDLING NULLS

# For Reasons: Replace nulls with 'N/A' so they can be used as filters in Power BI
df['Cancelled Rides by Customer'] = df['Cancelled Rides by Customer'].fillna(0)
df['Cancelled Rides by Driver'] = df['Cancelled Rides by Driver'].fillna(0)
df['Incomplete Rides'] = df['Incomplete Rides'].fillna(0)
df['Reason for cancelling by Customer'] = df['Reason for cancelling by Customer'].fillna('N/A')
df['Driver Cancellation Reason'] = df['Driver Cancellation Reason'].fillna('N/A')
df['Incomplete Rides Reason'] = df['Incomplete Rides Reason'].fillna('N/A')
df['Payment Method'] = df['Payment Method'].fillna('N/A')

# 5. REVENUE & DISTANCE FIX
# If a ride wasn't completed, Booking Value and Distance are usually NaN. 
# We'll set them to 0 to avoid errors in SUM calculations.
df['Booking Value'] = df['Booking Value'].fillna(0)
df['Ride Distance'] = df['Ride Distance'].fillna(0)

File_Name = 'cleaned_data.csv'

df.to_csv(OUTPUT_DIR / File_Name, index=False)
print('✅ Clean csv exported successfully')