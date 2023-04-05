n = int(input())
l2 = []
for _ in range(n):
    l2.append(int(input()))

l1 = list(range(1, max(l2)))

for i in l2:
    if i in l1:
        l1.remove(i)
l1.sort()


if len(l1) == 0:
    print('good job')
else:
    for j in l1:
        print(j)
