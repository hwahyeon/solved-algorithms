l = []
for _ in range(10):
    l.append(int(input()))
s = sum(l)
for i in l:
    if s-i == i:
        print(i)
        break
