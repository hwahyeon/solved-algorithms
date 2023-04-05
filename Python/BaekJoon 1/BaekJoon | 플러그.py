import sys
n = int(sys.stdin.readline())
res = 1 - n
for _ in range(n):
    res += int(sys.stdin.readline())
print(res)
