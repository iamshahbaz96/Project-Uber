SELECT `Pickup Location`, COUNT(`Booking ID`) as Total_Rides
FROM uber.cleaned_data
GROUP BY `Pickup Location`
ORDER BY Total_Rides DESC
LIMIT 5;