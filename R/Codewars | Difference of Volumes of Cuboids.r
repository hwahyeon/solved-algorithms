find_difference <- function(a, b){
   abs(a[1]*a[2]*a[3]-b[1]*b[2]*b[3])
}

# more intuitive way
find_difference <- function(a, b){
   abs(prod(a) - prod(b))
}
