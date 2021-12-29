is_triangle <- function(a, b, c){
 ifelse(a+b > c & a+c > b & b+c > a, TRUE, FALSE)
}
