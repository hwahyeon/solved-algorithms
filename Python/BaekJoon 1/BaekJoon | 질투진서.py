n, i, j = map(int, input().split())
c = []
for _ in range(n):
    c += list(map(int, input().split()))
jin = c[n*(i-1)+j-1]
t = []
t += c[n*(i-1):n*(i-1)+n]

for k in range(n):
    t.append(c[(j-1)+n*k])

cnt = 0
for l in t:
    if l > jin:
        cnt += 1
print('ANGRY') if cnt > 0 else print('HAPPY')
