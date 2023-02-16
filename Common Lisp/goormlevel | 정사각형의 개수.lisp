(setq n (read))
(setq *r* 0)

(loop for i from 1 to n
  do (setq *r* (+ *r* (* i i))) )

(write *r*)
