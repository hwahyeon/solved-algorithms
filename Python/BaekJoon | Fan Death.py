n = int(input())
r = 0
for i in range(1, n+1):
    if n%i == 0:
        r += i
print(r*5-24)
