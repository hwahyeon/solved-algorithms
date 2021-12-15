find_short <- function(s){
  r <- unlist(strsplit(s, " "))
  min(nchar(r))
}
