SELECT `Vehicle Type`, 
       (COUNT(CASE WHEN `Booking Status` = 'Cancelled by Customer' THEN 1 END) * 100.0 / COUNT(*)) as Cancel_Rate
FROM uber.cleaned_data
GROUP BY `Vehicle Type`;