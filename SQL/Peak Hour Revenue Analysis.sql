SELECT Time_Slot, SUM(`Booking Value`) as Total_Revenue
FROM uber.cleaned_data
WHERE ride_status = 'Ride complete'
GROUP BY Time_Slot
ORDER BY Total_Revenue DESC;