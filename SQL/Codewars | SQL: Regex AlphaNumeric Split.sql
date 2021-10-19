SELECT
  project,
  REGEXP_REPLACE(address,'[[:digit:]]','','g') letters,
  REGEXP_REPLACE(address,'[[:alpha:]]','','g') numbers
FROM repositories
