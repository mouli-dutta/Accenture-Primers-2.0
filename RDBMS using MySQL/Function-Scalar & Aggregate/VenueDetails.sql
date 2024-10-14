SELECT Venue_name, Venue_Cost,
  CASE
    WHEN Venue_Cost < 50000 THEN 'Low Cost'
    WHEN Venue_Cost BETWEEN 50000 AND 200000 THEN 'Medium Cost'
    WHEN Venue_Cost > 200000 THEN 'High Cost'
  END AS cost_category
  
FROM Venue_Master
ORDER BY Capacity DESC;
