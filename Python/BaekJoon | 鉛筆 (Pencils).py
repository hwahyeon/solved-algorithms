import math
n, a, b, c, d = map(int, input().split())
res = min(math.ceil(n/a) * b, math.ceil(n/c) * d)
print(res)
