N, W, H, L = map(int, input().split())
r = (W//L)*(H//L)
print(min(r, N))
