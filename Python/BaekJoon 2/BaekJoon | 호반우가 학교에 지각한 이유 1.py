ho = list(map(int, input().split()))
res = (4*ho[-1]) - sum(ho[:4])
print(0) if res <= 0 else print(res)
