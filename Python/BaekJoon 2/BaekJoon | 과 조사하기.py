a, b, c = 0, 0, 0
n = int(input())
for _ in range(n):
    gp, cp, np = map(int, input().split())
    if gp > 1:
        if cp == 1 or cp == 2:
            a += 1
        elif cp == 3:
            b += 1
        elif cp == 4:
            c += 1
print(a)
print(b)
print(c)
print(n - a - b - c)
