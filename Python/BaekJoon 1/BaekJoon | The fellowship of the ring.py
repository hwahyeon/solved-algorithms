W, N, P = map(int, input().split())
l = list(map(int, input().split()))
r = 0
for i in l:
    if W <= i <= N:
        r += 1
print(r)
