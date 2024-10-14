SELECT Venue_Id, Venue_name, (Venue_Cost + 100) AS New_Cost 
FROM Venue_Master
ORDER BY New_Cost ASC
LIMIT 2;
