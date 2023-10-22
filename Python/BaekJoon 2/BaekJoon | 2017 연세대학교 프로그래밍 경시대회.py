r = 0
n = int(input())
for i in range(2, n - 1, 2):
    r += (n - i - 2)//2
print(r)
