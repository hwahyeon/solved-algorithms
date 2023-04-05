N, L = input().split()
N = int(N)
r = 0
i = 0

while r != N:
    i += 1
    if L not in str(i):
        r += 1
print(i)
