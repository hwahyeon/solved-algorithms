N, M = map(int, input().split())
res = N
while 1:
    if N == 0:
        break
    else:
        N = N//M
        res += N
print(res)
