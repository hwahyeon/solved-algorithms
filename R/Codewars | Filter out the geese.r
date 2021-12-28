goose_filter <- function(birds){
  birds[! birds %in% c("African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher")]
}
