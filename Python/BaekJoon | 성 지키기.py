a, b = map(int, input().split())
M1 = []
for _ in range(a):
    M1.append(list(input()))

M2 = list(map(list, zip(*M1)))
r1, r2 = 0, 0
for i in M1:
    if 'X' not in i:
        r1 += 1

for i in M2:
    if 'X' not in i:
        r2 += 1

print(max(r1, r2))
