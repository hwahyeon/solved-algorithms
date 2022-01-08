spoonerize <- function(words) {
  x <- unlist(strsplit(words, " "))
  fir <- x[1]
  end <- tail(x, n=1)

  x[1] <- paste0(substring(end, 1, 1), substring(fir, 2))
  x[length(x)] <- paste0(substring(fir, 1, 1), substring(end, 2))

  paste(x, collapse=" ")
}
