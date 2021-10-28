SELECT
  c.customer_id,
  c.email,
  COUNT(p.customer_id)::INT as payments_count,
  SUM(p.amount)::FLOAT AS total_amount
FROM
  customer as c,
  payment as p
WHERE
  c.customer_id = p.customer_id
GROUP BY
  c.customer_id
ORDER BY
  total_amount DESC
LIMIT 10;
