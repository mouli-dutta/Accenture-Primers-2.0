SELECT
  enquiry_id,
  cust_id,
  concat(monthname(Start_Date), ',', year(Start_Date)) AS Event_Date

FROM Enquiry_Master

WHERE year(Start_Date) > 2015

ORDER BY 
  Event_Date ASC,
  cust_id ASC;
