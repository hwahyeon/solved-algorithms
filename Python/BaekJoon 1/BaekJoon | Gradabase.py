res = []
cnt = 0
for _ in range(int(input())):
    cnt += 1
    res.append(f'Case {cnt}:')
    for i in range(int(input())):
        n = int(input())
        if n <= 5:
            res.append(n+1)
for j in res:
    print(j)
