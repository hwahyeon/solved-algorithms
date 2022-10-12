C, K, P = map(int, input().split())
w = 0
for i in range(1, C+1):
    w += K*i+P*i**2
print(w)
