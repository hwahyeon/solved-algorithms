generate_shape <- function(n){
  x <- paste(replicate(n, "+"), collapse = "")
  print(paste(replicate(n, x), collapse = "\\n"))
}
