get_grade <- function(a, b, c) {
  n <- (a+b+c)/3
  if (n == 0){
    'F'
  } else {
  c('F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A')[n %/% 10]
  }
}
