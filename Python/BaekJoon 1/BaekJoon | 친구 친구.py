import sys
n, m = map(int, sys.stdin.readline().split())
lst = [0]*n
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    lst[a-1] += 1
    lst[b-1] += 1
for j in lst:
    print(j)
