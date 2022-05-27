n = int(input())
l = input()
res = 0

for i in range(n-4):
    d = l[i:i+5]
    c = 0
    for j in range(4):
        if abs(ord(d[j])-ord(d[j+1])) == 1:
            c += 1
        if c == 4:
            res += 1
