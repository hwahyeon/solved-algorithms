n, r = map(int, input().split())
l = list(map(int, input().split()))
m = sum(l[:r])
for i in range(n-r+1):
    s = sum(l[i:i+r])
    if m < s:
        m = s
print(m)
