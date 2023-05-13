n = int(input())

c = 0
if n <= 198:
    for i in range(100):
        for j in range(100):
            if i + j == n:
                c += 1
print(c)
