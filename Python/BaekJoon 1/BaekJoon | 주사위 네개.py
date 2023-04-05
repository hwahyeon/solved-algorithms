res = 0

for _ in range(int(input())):
    d = sorted(list(map(int, input().split())))

    if d[0]==d[1]==d[2]==d[3]:
        best = 50000 + d[0] * 5000
        if best > res:
            res = best
    elif (d[0]==d[1]==d[2] or d[1]==d[2]==d[3]):
        best = 10000 + d[1] * 1000
        if best > res:
            res = best
    elif d[0] == d[1] and d[2] == d[3]:
        best = 2000+d[1]*500 + d[2]*500
        if best > res:
            res = best
    elif (d[0]==d[1] or d[1]==d[2]):
        best = 1000 + d[1]*100
        if best > res:
            res = best
    elif d[2]==d[3]:
        best = 1000 + d[3]*100
        if best > res:
            res = best
    elif d[0]!=d[1]!=d[2]!=d[3]:
        best = max(d) * 100
        if best > res:
            res = best
print(res)
