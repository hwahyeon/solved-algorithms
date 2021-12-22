enough <- function(cap, on, wait){
  res <- cap-on-wait
  ifelse(res>0, 0, abs(res))
}
