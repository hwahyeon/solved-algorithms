n = input()
l = list(map(int, input().split()))
c, t = 0, 1

for i in l:
    if i != t:
        c += 1
    else:
        t += 1
print(c)
