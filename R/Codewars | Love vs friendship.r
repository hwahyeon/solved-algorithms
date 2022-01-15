words_to_marks <- function(s){
  lst <- c('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
  res <- 0
  x <- unlist(strsplit(s, split=''))
  for(i in x){res = res + which(lst == i)}
  res
}
