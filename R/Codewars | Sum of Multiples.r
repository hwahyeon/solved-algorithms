# 시간초과
sum_mul <- function(n, m){
  if (m <= 0){
    print("INVALID")
  }
  else {
    i = 1
    res = 0
    while(m > (n*i)){
      res = res + (n*i)
      i = i + 1
    }
    print(res)
  }
}

# 정답
sum_mul <- function(n, m){
  if (m <= 0 | n <= 0){
    print("INVALID")
  }
  else {
    i = ceiling(m/n)-1
    print(n * (i*(i+1)/2))
  }
}
