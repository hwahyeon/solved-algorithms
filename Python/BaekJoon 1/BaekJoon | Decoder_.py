n = int(input())
l = input().split()
r = l[0][0]

for i in range(n - 1):
    pre = len(l[i])
    if pre > len(l[i + 1]):
        r += ' '
    else:
        r += l[i+1][pre-1]

print(r)
