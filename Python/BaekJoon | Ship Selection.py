for _ in range(int(input())):
    N, D = map(int, input().split())
    res = 0
    for _ in range(N):
        v, f, c = map(int, input().split())
        if v * f / c >= D:
            res += 1
    print(res)
