(setq n (read))
(if (= (mod n 2) 0)
		(write-string "even")
		(write-string "odd"))
