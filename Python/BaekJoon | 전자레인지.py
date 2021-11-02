t = int(input())
a, b, c = 0, 0, 0
while 1:
    if t >= 300:
        t = t - 300
        a += 1
    elif t >= 60:
        t = t - 60
        b += 1
    elif t >= 10:
        t = t - 10
        c += 1
    else:
        break
if t == 0:
    print(a, b, c)
else:
    print(-1)
