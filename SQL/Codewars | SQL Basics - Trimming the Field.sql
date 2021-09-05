SELECT id, name, split_part(characteristics, ',', 1) characteristic
FROM monsters
ORDER BY id
