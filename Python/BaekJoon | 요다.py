for _ in range(int(input())):
    l = list(input().split())
    print(*l[2:], *l[:2])
