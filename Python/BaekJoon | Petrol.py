n = int(input())
k = int(input())
r = min(k + 60, n)
print(r*1500 + (n - r)*3000)
