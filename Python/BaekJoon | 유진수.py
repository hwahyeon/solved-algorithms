n = input()
l = len(n)
res = 0
for i in range(1, l):
    a, b = n[:i], n[i:]
    ra, rb = 1, 1
    for j in a:
        ra *= int(j)
    for k in b:
        rb *= int(k)
    if ra == rb:
        res += 1
        break
print('YES') if res > 0 else print('NO')
