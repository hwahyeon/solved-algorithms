SELECT
  CHAR_LENGTH(name) as id,
  CHAR_LENGTH(CAST(legs AS CHAR(10))) as name,
  CHAR_LENGTH(CAST(arms AS CHAR(10))) as legs,
  CHAR_LENGTH(characteristics) as arms,
  CHAR_LENGTH(CAST(id AS CHAR(10))) as characteristics
FROM monsters;
