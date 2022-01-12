sum_triangular_numbers <- function(n){
  res <- 0
  if(n<0){0}
  else{for(i in 1:n){res <- res + sum(1:i)}
    res}
}
