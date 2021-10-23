SELECT
  name,
  weight,
  price,
  CAST(
    ROUND(
      CAST((price/(weight/1000)) as numeric),
      2)
    AS real)
    AS price_per_kg
FROM Products
ORDER BY price_per_kg, name
