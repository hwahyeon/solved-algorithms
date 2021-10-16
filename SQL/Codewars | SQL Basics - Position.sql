SELECT
  m.id,
  m.name,
  POSITION(',' IN m.characteristics) comma
FROM monsters m
ORDER BY comma;
