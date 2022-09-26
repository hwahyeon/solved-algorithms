a = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            a[i][j] = 1

print(sum(sum(a,[])))
