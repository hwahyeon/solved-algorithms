#1
grow <- function(arr) {
  res <- 1
  for(i in arr){
    res <- res * i
  }
  print(res)
}

#2
grow <- function(arr) {
  prod(arr)
}
