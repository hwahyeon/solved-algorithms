while 1:
    N, M = map(int, input().split())
    if N == M == 0:
        break

    L = list(map(int, input().split()))
    pay = M // N 
    t = 0

    for money in L:
        if money < pay:
            t += money
        else:
            t += pay

    print(t)
