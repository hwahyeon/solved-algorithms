while 1:
    C, W, L, P = map(int, input().split())
    if C == W == L == P == 0:
        break
    print(C ** (W * L * P))
