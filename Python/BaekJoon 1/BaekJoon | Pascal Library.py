while 1 :
    n, d = map(int, input().split())
    if n == d == 0:
        break
    r = [0] * n
    for _ in range(d) :
        l = list(map(int, input().split()))
        r = [x + y for x, y in zip(r, l)]
    if d in r:
        print("yes")
    else:
        print("no")
