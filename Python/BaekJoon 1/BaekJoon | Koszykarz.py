k, w, m = map(int, input().split())
if (w - k)%m:
    r = (w - k)//m + 1
else:
    r = (w - k)//m
print(r)
