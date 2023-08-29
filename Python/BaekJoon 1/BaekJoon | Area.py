r = 0
for _ in range(int(input())):
    h, w = map(int, input().split())
    r = max(r, h * w)
print(r)
