/* your query - you are given columns a, b, and c  */
SELECT
  GREATEST(
    a + b + c,
    a * (b + c),
    a * b * c,
    a + b * c,
    (a + b) * c) as res
FROM expression_matter;
