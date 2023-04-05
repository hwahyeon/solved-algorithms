n = int(input())
d = 5
for i in range(1, n):
    d += (i+2)*3-2
print(d % 45678)
