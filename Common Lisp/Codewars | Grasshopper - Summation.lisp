(defpackage #:challenge/solution
  (:use #:cl)
  (:export #:summation))
(in-package #:challenge/solution)

(defun summation (n)
  (loop for i
        below (+ n 1)
        sum i))
