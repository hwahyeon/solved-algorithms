SELECT
  RANK()
  OVER (
    ORDER BY
      sum(points) DESC
    ) as rank,
  COALESCE(NULLIF(clan, ''), '[no clan specified]') as clan,
  SUM(points) as total_points,
  COUNT(clan) as total_people
FROM people
GROUP BY clan
