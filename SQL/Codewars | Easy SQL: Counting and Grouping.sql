SELECT race, count(race) as count FROM demographics
GROUP BY race
ORDER BY count DESC
