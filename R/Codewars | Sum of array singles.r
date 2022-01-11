repeats <- function(arr){
  sum(arr[! arr %in% arr[-pmatch(unique(arr),arr)]])
}
