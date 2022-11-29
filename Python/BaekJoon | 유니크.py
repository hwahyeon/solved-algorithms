n = int(input())
rnd = [[],[],[]]
for _ in range(n):
    r1, r2, r3 = map(int, input().split())
    rnd[0].append(r1)
    rnd[1].append(r2)
    rnd[2].append(r3)

res = [0] * n
for i in range(3):
    for j in range(n):
        if rnd[i].count(rnd[i][j]) == 1:
            res[j] += rnd[i][j]

for k in res:
    print(k)
