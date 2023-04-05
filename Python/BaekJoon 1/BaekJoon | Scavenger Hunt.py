n1, n2 = map(int, input().split())

a = []
b = []
for k in range(1, n1+1):
    if n1 % k == 0:
        a.append(k)
for m in range(1, n2+1):
    if n2 % m == 0:
        b.append(m)
for i in range(len(a)):
    for j in range(len(b)):
        print(a[i], b[j])
