(setq n (read))
(defparameter *res* 0)
(dotimes (i n) (defparameter *res* (+ *res* i)))
(write *res*)
