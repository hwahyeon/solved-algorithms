n = int(input())
lst = list(map(int, input().split()))
r = []
for i in lst:
    if i < 250:
        r.append(4)
    elif i < 275:
        r.append(3)
    elif i < 300:
        r.append(2)
    else:
        r.append(1)

print(*r)
