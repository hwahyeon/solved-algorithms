A, B, C = map(int, input().split())
r = 1
odd = 0
if A%2 != 0:
    r *= A
    odd += 1
if B%2 != 0:
    r *= B
    odd += 1
if C%2 != 0:
    r *= C
    odd += 1
if r == 1 and odd == 0:
    r = A*B*C
print(r)
