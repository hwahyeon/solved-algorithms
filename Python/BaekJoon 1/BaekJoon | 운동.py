N, m, M, T, R = map(int, input().split())
c, tm = 0, 0
cur = m

while tm < N:
    if m + T > M:
        break
    if cur + T <= M:
        cur += T
        tm += 1
    else:
        cur = max(cur - R, m)
    c += 1
print(c if tm == N else -1)
