a, b = map(int, input().split())
min = a/b
n = int(input())

for i in range(n):
    c, d = map(int, input().split())
    if min > c/d:
        min = c/d

print(min*1000)
