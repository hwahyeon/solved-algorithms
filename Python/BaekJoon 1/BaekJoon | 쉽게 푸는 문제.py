a, b = map(int, input().split())

lst = []
for i in range(46):
    for j in range(i):
        lst.append(i)

print(sum(lst[a-1:b]))
