n, m = map(int, input().split())
for i in range(n):
    if i%2 == 0:
        print(('*.'*m)[:m])
    else:
        print(('.*'*m)[:m])
