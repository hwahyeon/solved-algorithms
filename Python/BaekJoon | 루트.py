while 1:
    B, N = map(int, input().split())
    if B == N == 0:
        break
    A = 0
    while A**N <= B:
        A += 1
    if abs((A**N)-B) < abs(((A-1)**N)-B):
        print(A)
    else:
        print(A-1)
