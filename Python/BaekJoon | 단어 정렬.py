import sys

res = [sys.stdin.readline().strip() for i in range(int(sys.stdin.readline()))]
res = sorted(list(set(res)))
res.sort(key = len)
for i in res:
    print(i)
