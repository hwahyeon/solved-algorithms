SELECT
  project,
  commits,
  contributors,
  REGEXP_REPLACE(address, '[[:digit:]]', '!', 'g') as address
FROM repositories;
