res = float('inf')

for _ in range(int(input())):
    t, l = map(int, input().split())
    res = min(res, t + l)

print(res)
