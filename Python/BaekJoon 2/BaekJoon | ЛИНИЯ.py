N = int(input())

while N != 2 and (N - 1) % 2 == 0:
    N = (N - 1) // 2 + 1

print(N)
