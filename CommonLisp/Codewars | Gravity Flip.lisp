(defpackage #:challenge/solution
  (:use #:cl)
  (:export #:flip))
(in-package #:challenge/solution)

(defun flip (dir boxes)
  (if (string= dir "R")
   (sort boxes #'<)
   (sort boxes #'>)
   )
  )
