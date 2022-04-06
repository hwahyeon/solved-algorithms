l = []
for x in input():
   l.append(ord(x) - 96)

cnt = 1
for i in range(len(l)-1):
    if l[i] >= l[i+1]:
        cnt += 1

print(cnt)
