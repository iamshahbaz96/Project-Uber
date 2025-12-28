📂 Uber NCR Booking Analysis (End-to-End)
📌 Project Overview
This project provides a comprehensive end-to-end data analysis of Uber booking data in the Delhi-NCR region. It tracks the entire data lifecycle: from raw data cleaning in Python, to structured querying in SQL, and finally, interactive storytelling in Power BI.

🛠️ Tech Stack
Python: Data Wrangling, Cleaning, and Feature Engineering.

SQL (MySQL/PostgreSQL): Database Management and Complex Analytical Queries.

Power BI: DAX Measures, Data Modeling (Star Schema), and Interactive Dashboards.

🚀 The Workflow
1. Data Cleaning & Engineering (Python)
The raw dataset was messy, containing inconsistent formats and missing values. I used Python (Pandas) to:

Standardized Booking ID and Customer ID formats.

Created a unified Pickup_DateTime object to handle time-series analysis.

Feature Engineering: Developed custom columns like Time_Slot (Morning Rush, Evening Rush) and Day_of_Week to identify peak demand patterns.

Handled null values in ratings and cancellation reasons to ensure dashboard accuracy.

2. Analytical Deep Dive (SQL)
After cleaning, the data was migrated to a SQL environment. I wrote queries to extract high-level business KPIs:

Success Rate: Calculated the percentage of completed vs. cancelled rides.

Revenue Leakage: Analyzed the financial impact of "Driver Cancellations" in specific hubs like Gurgaon and Noida.

Regional Demand: Identified the top 5 highest-demand pickup locations in NCR.

3. Visual Storytelling (Power BI)
I built a 3-page interactive dashboard focusing on:

Executive Summary: High-level KPIs (Total Revenue, Avg Ratings, Booking Volume).

Regional Performance: A map-based view of NCR ride density.

Operational Efficiency: Analysis of VTAT (Vehicle Arrival Time) and CTAT (Customer Arrival Time).

📊 Key Business Insights
Peak Hours: 60% of cancellations in Gurgaon occur during the "Morning Rush" (8 AM - 11 AM).

Vehicle Performance: Uber Auto has a 15% higher completion rate in Old Delhi compared to Go Sedan.

Payment Trends: UPI has overtaken Cash as the preferred payment method, accounting for 45% of total revenue.

📂 Repository Structure
Plaintext

├── data/
│   └── ncr_ride_bookings.csv      # Raw Data
├── codes/
│   ├── data_cleaning.py           # Cleaning script
│   ├── ImportFromSQL.py           # Import from SQL script
│   └── ImportToSQL.py             # Import to SQL script
├── output
│   └── cleaned_data.csv           # Clean Data 
├── SQL/
│   └── Cancellation Rate by Vehicle Type.sql       # Cancellation Rate queries
│   ├── Peak Hour Revenue Analysis.sql              # Peak Hour Analysis queries
│   └── Top 5 High-Demand Pickup Locations.sql      # High Demand queries 
├── powerbi/
│   └── Dashboard.pbix    # Power BI File
└── README.md
👤 Author
[Shahbaz Ahmed](https://www.linkedin.com/in/shahbaz-ahmed-9a239b131/)
