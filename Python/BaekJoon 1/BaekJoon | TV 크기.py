D, H, W = map(int, input().split())
X = (D**2 / (H**2 + W**2))**0.5
print(int(H*X), int(W*X))
