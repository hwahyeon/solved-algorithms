sm, sb = map(int, input().split())
x = (sm + sb)//2
y = sm - x
if x < 0 or y < 0 or (sm + sb)%2:
    print(-1)
else:
    print(max(x, y), min(x, y))
