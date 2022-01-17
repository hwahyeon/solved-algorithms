get_middle <- function(s){
  x <- unlist(strsplit(s, split=''))
  l <- length(x)
  ifelse(l %% 2 == 0,
         paste0(x[(l/2):(l/2+1)], collapse=""),
         x[ceiling(l/2)])
}
