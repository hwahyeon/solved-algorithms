res = []
for i in range(7):
    n = int(input())
    if n % 2 != 0:
        res.append(n)
res.sort()
if len(res) == 0:
    print(-1)
else:
    print(sum(res))
    print(res[0])
