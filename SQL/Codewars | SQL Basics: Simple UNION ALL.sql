SELECT
  'US' as location,
  id,
  name,
  price,
  card_name,
  card_number,
  transaction_date
FROM ussales
WHERE price >= 50
UNION ALL
SELECT
  'EU' as location,
  id,
  name,
  price,
  card_name,
  card_number,
  transaction_date
FROM eusales
WHERE price >= 50
ORDER BY
  location DESC, id;
