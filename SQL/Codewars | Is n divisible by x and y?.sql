-- you will be given a table 'kata' with columns 'n', 'x', and 'y'. Return the 'id' and your result in a column named 'res'.
select
  id,
  CASE WHEN n%x != 0 OR n%y != 0 THEN false
    ELSE true
  END as res
from kata
