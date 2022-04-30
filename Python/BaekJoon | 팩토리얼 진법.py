# 1
import sys
input = sys.stdin.readline

while 1:
    n = input().rstrip()
    if n == '0':
        break
    else:
        f = [1, 2, 6, 24, 120]
        res = 0
        for s, i in enumerate(n[::-1]):
            res += f[s]*int(i)
        print(res)

# 2
import sys
input = sys.stdin.readline

while 1:
    n = input().rstrip()
    if n == '0':
        break
    else:
        f = 1
        res = 0
        for s, i in enumerate(n[::-1]):
            f *= (s+1)
            res += f*int(i)
        print(res)
