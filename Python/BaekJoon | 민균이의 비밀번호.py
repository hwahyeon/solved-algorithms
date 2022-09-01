n = int(input())
w = []
for _ in range(n):
    w.append(input())

for i in w:
    if i[::-1] in w:
        l = len(i)
        s = i[int(l/2)]
        break
print(l, s)
