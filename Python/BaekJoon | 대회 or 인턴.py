N, M, K = map(int, input().split())
r = 0
while 1:
    N -= 2
    M -= 1
    if N < 0 or M < 0 or N+M < K: break
    r += 1
print(r)
