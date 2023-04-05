res = []
for _ in range(3):
    a, b = map(int, input().split())
    if 10 * a >= 5000:
        res.append((10 * b)/(10 * a - 500))
    else:
        res.append(b/a)

print(['S', 'N', 'U'][res.index(max(res))])
