n = int(input())
r1, r2 = [], []
s = 0
for _ in range(n):
    r1.append(input())
for _ in range(n):
    r2.append(input())    
for i in range(n):
    if r1[i] == r2[i]:
        s += 1
print(s)
