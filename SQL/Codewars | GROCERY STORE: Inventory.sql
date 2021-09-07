SELECT id, name, stock
FROM products
WHERE producent in ('CompanyA')
  and stock <3
ORDER BY id
