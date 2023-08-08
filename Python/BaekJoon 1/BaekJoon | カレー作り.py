def result(A, B, C, D):
    k = (B * C - A) // D
    p = (B * C - A) % D

    if k < 0:
        return 0
    else:
        if p == 0:
            return k
        else:
            return k + 1

while True:
    A, B, C, D = map(int, input().split())
    if A == 0 and B == 0 and C == 0 and D == 0:
        break
    else:
        print(result(A, B, C, D))
