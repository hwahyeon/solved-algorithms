SELECT 
  DATE(s.transaction_date) AS day,
  d.name AS department,
  COUNT(s.id) AS sale_count
FROM department AS d
    INNER JOIN sale AS s ON d.id = s.department_id
GROUP BY day, d.name
ORDER BY day;
