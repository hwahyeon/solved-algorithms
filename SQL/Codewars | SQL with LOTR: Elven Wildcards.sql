SELECT
  INITCAP(firstname)||' '||INITCAP(lastname) as shortlist
FROM Elves
WHERE
  firstname LIKE '%tegil%' OR lastname LIKE '%astar%'
