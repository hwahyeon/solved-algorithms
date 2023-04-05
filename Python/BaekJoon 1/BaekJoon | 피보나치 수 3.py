n = int(input())

a, b = 0, 1
m = 1000000
n %= 1500000

for _ in range(n):
    a, b = b%m, (a+b)%m
print(a)
