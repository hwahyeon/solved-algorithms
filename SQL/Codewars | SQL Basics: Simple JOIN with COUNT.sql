SELECT p.id, p.name, COUNT(t.id) as toy_count
FROM people as p
LEFT JOIN toys as t
ON p.id = t.people_id
group by p.id
