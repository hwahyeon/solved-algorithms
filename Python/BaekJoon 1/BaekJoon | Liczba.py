n = int(input())
r1, r2 = 0, 0
for i in range(2, n):
    if n % i != 0:
        r1 = i
        break
for j in reversed(range(2, n)):
    if n % j != 0:
        r2 = j
        break
print(r1, r2)
