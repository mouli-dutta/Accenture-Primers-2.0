SELECT Venue_Id, Venue_name, Venue_Cost, Location
FROM Venue_Master
WHERE Capacity BETWEEN 1000 AND 20000
ORDER BY Venue_name ASC
