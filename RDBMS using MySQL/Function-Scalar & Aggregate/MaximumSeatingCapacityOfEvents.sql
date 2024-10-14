SELECT
  Event_Id,
  max(Capacity) AS maximum_seating_capacity
FROM Venue_Master   
WHERE Wifi = 'Yes'
GROUP BY Event_Id
ORDER BY maximum_seating_capacity DESC;
