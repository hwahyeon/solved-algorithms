a, b = map(int, input().split())
res = [[] for i in range(b)]
for _ in range(a):
    s = input()
    s = s.translate(s.maketrans("-|^<v>/\\", "|-<v>^\\/", ""))
    for i in range(b):
        res[i].append(s[i])

for j in res[::-1]:
    print(*j, sep='')
