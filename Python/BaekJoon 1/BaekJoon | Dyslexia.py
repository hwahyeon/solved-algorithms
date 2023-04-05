n = int(input())
r = 0
s1, s2 = input(), input()
for i in range(n):
    if s1[i] != s2[i]:
        r += 1
print(r)
