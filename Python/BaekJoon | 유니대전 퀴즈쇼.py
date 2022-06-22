s, n = map(str, input().split())
lsta = []
lstb = []
for _ in range(int(s)):
    a, b = input().split()
    lsta.append(a)
    lstb.append(b)
print(lstb[:lsta.index(n)].count(lstb[lsta.index(n)]))
