library(stringr)
expand <- function(s){
  unlist(str_split(s,""))
}
