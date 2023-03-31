n = int(input())
m = []
for _ in range(n):
    m.append(input())
k = int(input())

if k == 1:
    print(*m, sep='\n')
elif k == 2:
    r = []
    for i in m:
        r.append(i[::-1])
    print(*r, sep='\n')
else:
    print(*m[::-1], sep='\n')
