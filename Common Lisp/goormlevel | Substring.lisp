(setq n (read-line))
(setq s (read))
(setq e (read))
(write-string (subseq n (- s 1) (- (+ s e) 1 )))
