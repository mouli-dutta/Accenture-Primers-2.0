SELECT
  C_first_name AS user_name,
  contact
  (
    substring(C_first_name, 1, 3),
    substring(phoneno, 5, 2)
  ) AS password

FROM Customer_Master
WHERE Email LIKE '%gmail.com'
ORDER BY user_name ASC;
