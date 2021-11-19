SELECT
  p.id,
  p.name,
  RANK()
    OVER (PARTITION BY p.id ORDER BY p.id DESC) as sale_rank,
  COUNT(s.sale) as sale_count
FROM
  people as p
INNER JOIN sales as s ON s.people_id = p.id
GROUP BY
  p.id;
