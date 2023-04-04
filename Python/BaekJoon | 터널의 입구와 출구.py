n = int(input())
t = []
t.append(int(input()))
for i in range(n):
    a, b = map(int, input().split())
    t.append(t[i] + a - b)

for i in range(n + 1):
    if t[i] < 0:
        print(0)
        exit()
print(max(t))
