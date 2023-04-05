H, W = map(int, input().split())
o1, o2 = '', ''
for _ in range(H):
    o1 += input()
input()
for _ in range(H):
    o2 += input()
c = 0
for i in range(H*W):
    if o1[i] == o2[i]:
        c += 1
print(c)
