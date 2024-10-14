SELECT C_first_name, Phoneno, Gender
FROM Customer_Master
WHERE C_last_name IS NULL OR C_middle_name IS NULL
ORDER BY Phoneno ASC;
