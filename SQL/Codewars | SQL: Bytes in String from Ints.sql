SELECT
  LENGTH(CAST(number1 AS TEXT)) AS octnum1,
  LENGTH(CAST(number2 AS TEXT)) AS octnum2,
  LENGTH(CAST(number3 AS TEXT)) AS octnum3,
  LENGTH(CAST(number4 AS TEXT)) AS octnum4,
  LENGTH(CAST(number5 AS TEXT)) AS octnum5
FROM numbers;
