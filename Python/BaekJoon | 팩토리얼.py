# for 문

n = int(input())
res = 1
for i in range(1, n):
    res += i*res
print(res)


# 내장 함수

import math
print(math.factorial(int(input())))
