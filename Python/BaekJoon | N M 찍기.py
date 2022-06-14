N, M = map(int, input().split())
cnt = 0
for i in range(N):
    l = []
    for j in range(M):
        cnt += 1
        l.append(cnt)
    print(*l)
