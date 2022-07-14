l = []
for _ in range(10):
    l.append(int(input()))
print(int(sum(l)/len(l)))
fre = 0
most = 0
for i in set(l):
    if fre < l.count(i):
        fre = l.count(i)
        most = i
print(most)
