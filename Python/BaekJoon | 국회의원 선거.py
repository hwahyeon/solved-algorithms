cnt = 0
c = []
for _ in range(int(input())):
    c.append(int(input()))

if len(c) == 1:
    print(0)
else:
    dasom = c[0]
    can = c[1:]
    can.sort()
    while 1:
        if dasom > can[-1]:
            print(cnt)
            break
        else:
            dasom += 1
            can[-1] -= 1
            can.sort()
            cnt += 1
