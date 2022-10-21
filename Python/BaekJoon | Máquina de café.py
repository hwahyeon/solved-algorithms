l = []
for _ in range(3):
    l.append(int(input()))

print(min(l[0]*2 + l[1], l[0] + l[2], l[1] + l[2]*2)*2)
