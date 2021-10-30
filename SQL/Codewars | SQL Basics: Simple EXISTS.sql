SELECT
  d.id,
  d.name
FROM
  departments as d
WHERE EXISTS
  (SELECT 1
   FROM sales as s
   WHERE d.id = s.department_id AND price > 98)
