m = 0
for _ in range(int(input())):
    a, d, g = map(int, input().split())
    s = a * (d + g)
    if a == d+g:
        s *= 2
    if s > m:
        m = s
print(m)
