for _ in range(int(input())):
    lst = list(input().split())
    res = []
    for s in lst:
        res.append(s[::-1])
    print(" ".join(res))
