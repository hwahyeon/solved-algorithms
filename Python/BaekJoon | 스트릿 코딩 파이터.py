A, B, C = map(int, input().split())

res = 0
for i in range(int(input())):
    t = 0
    for j in range(3):
        a, b, c = map(int, input().split())
        t += (A*a + B*b + C*c)
    if t > res:
        res = t

print(res)
