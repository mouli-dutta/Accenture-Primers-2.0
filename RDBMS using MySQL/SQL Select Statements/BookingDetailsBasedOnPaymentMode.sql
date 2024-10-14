SELECT Booking_Id, Enquiry_Id, Total_amount
FROM Booking_Master
WHERE Mode_of_Pay = 'Cash' OR Mode_of_Pay = 'Credit'
ORDER BY Enquiry_Id ASC;
