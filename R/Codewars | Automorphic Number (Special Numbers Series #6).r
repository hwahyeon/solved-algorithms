automorphic <- function(n) {
  x <- unlist(strsplit(as.character(n**2), split=''))
  p <- paste(tail(x, nchar(n)), collapse='')
  ifelse(as.character(n)==p, "Automorphic", "Not!!")
}
