X, L, R = map(int, input().split())

if L < X < R:
    print(X)
else:
    L1 = abs(X-L)
    R1 = abs(X-R)
    print(L) if L1 < R1 else print(R)
