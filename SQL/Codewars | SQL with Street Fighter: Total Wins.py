--- 3, 2, 1, fight! ---
SELECT
  name,
  SUM(won) as won,
  SUM(lost) as lost
FROM
  fighters
INNER JOIN winning_moves ON fighters.move_id = winning_moves.id
WHERE NOT
  winning_moves.move IN ('Hadoken', 'Shouoken', 'Kikoken')
GROUP BY
  name
ORDER BY
  won DESC
LIMIT 6;
