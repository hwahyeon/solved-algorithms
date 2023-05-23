n = int(input())
a = input()
b = input()
r = 0

if len(a) < len(b):
    a + ' ' * (len(a) - len(b))
for i in range(n):
    if a[i] == b[i]:
        r += 1

print(r)
