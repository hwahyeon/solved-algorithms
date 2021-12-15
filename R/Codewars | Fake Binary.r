fake_bin <- function(x){
  dict_ <- list(c('0','1','2','3','4'), c('5','6','7','8','9'))
  for (i in 1:5){x <- gsub(pattern = dict_[[1]][i], replacement = "0", x)}
  for (i in 1:5){x <- gsub(pattern = dict_[[2]][i], replacement = "1", x)}
  return(x)
}
