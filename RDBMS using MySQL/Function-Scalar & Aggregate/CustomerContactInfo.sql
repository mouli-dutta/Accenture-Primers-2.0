SELECT Cust_Id, C_first_name, COALESCE(city, phoneno, email) contact_info
FROM Customer_Master
ORDER BY contact_info;
