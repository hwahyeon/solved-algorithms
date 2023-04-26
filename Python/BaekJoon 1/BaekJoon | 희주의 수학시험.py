A, B = map(int, input().split())
r = []
for i in range(1, B+1):
    if len(r) < B:
        for _ in range(i):
            r.append(i)

print(sum(r[A-1:B]))
