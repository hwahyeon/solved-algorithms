for _ in range(int(input())):
    n = input()
    l = sorted(list(map(int, input().split())))
    print((l[-1] - l[0])*2)
