n = int(input())
f1 = input()
f2 = f1[::-1]
r = 0
for i in range(n//2):
    if f1[i] != f2[i]:
        r += 1
print(r)
