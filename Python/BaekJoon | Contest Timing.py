D, H, M = map(int, input().split())
t = (D*24*60 + H*60 + M) - (11*24*60 + 11*60 + 11)
print(-1) if t < 0 else print(t)
