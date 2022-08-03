N, M = map(int, input().split())
M1, M2 = [], []
for _ in range(N):
    M1.append(list(map(int, input().split())))
for _ in range(N):
    M2.append(list(map(int, input().split())))

for i in range(N):
    res = [i+j for i, j in zip(M1[i], M2[i])]
    print(*res)
