SELECT C_first_name, C_last_name, Street, City
FROM Customer_Master
WHERE C_first_name LIKE '_m%'
ORDER BY C_first_name;
