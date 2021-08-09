library(stringr)
no_space <- function(x){
  return(str_replace_all(x,' ',''))
}
