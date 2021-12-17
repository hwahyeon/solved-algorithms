abbrev_name <- function(name){
  n <- unlist(strsplit(name, " "))
  toupper(paste(substring(n, 1, 1), collapse='.'))
}
