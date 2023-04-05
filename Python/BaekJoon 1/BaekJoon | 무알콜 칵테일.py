a, b, c = map(int, input().split())
i, j, k = map(int, input().split())

q = min(a/i, b/j, c/k)
print(a-q*i, b-q*j, c-q*k)
