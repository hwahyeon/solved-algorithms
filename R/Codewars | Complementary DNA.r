DNA_strand <- function(dna){

  vec <- unlist(strsplit(dna, ""))
  n <- length(vec)

  for (i in 1:n){
         if(vec[i] == "A"){vec[i] <- "T"}
    else if(vec[i] == "T"){vec[i] <- "A"}
    else if(vec[i] == "C"){vec[i] <- "G"}
    else if(vec[i] == "G"){vec[i] <- "C"}
  }

  paste(vec, collapse='')
}
