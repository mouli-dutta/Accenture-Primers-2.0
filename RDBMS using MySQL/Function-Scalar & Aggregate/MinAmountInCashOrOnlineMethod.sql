SELECT 
  mode_of_pay,
  min(total_amount) as MINIMUM_TOTAL_AMOUNT
FROM Booking_Master
WHERE mode_of_pay IN ('Cash', 'Online')
GROUP BY mode_of_pay
ORDER BY MINIMUM_TOTAL_AMOUNT;
