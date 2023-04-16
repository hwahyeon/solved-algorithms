for _ in range(int(input())):
    n = int(input())
    t = 0
    while 1:
        if (t+1) + (t+1)**2 > n:
            break
        t += 1
    print(t)
