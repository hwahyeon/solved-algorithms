SELECT i as prime
FROM
  generate_series(2, 100) as i
WHERE
  i IN (2,3,5,7) OR
  i % 2 != 0 and
  i % 3 != 0 and
  i % 5 != 0 and
  i % 7 != 0
