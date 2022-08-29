l = []
for _ in range(9):
    l += list(map(int, input().split()))

print(max(l))
n = l.index(max(l))
print(n//9+1, n%9+1)
