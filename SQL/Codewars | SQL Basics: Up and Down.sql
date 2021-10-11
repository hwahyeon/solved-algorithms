SELECT 
  (CASE WHEN (sum(number1))%2 = 0 THEN MAX(number1)
        ELSE MIN(number1)
  END) as number1,
  (CASE WHEN (sum(number1))%2 = 0 THEN MAX(number2)
        ELSE MIN(number2)
  END) as number2
FROM numbers;
