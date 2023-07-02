from sys import stdin

n = int(stdin.readline().strip())
res = 1001
for i in range(n):
    a, b = map(int, stdin.readline().split())
    if b >= a:
        if b < res:
            res = b
if res == 1001:
    print(-1)
else:
    print(res)
