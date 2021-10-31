SELECT
  age,
  COUNT(name) AS total_people
FROM people
GROUP BY age 
HAVING COUNT(name) >= 10;
