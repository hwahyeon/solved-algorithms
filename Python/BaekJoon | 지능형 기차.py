tot, res = 0, 0
for i in range(4):
    a, b = map(int, input().split())
    tot += (b - a)
    if res < tot:
        res = tot
print(res)
