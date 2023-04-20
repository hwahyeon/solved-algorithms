e, f, c = map(int, input().split())

r = e + f
can = 0

while 1:
    if r < c:
        break
    else:
        can += r//c
        r = r//c + r % c
print(can)
