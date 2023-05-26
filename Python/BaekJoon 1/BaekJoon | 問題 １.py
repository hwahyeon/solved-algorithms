res1, res2 = 0, 0

for _ in range(int(input())):
    a, b = map(int, input().split())

    if a > b:
        res1 += (a + b)
    elif a < b:
        res2 += (a + b)
    else:
        res1 += a
        res2 += b

print(res1, res2)
