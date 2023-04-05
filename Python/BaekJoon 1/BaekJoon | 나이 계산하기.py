y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

if m1 < m2:
    print(y2-y1)
elif m1 == m2:
    if d1 <= d2:
        print(y2-y1)
    else:
        print(y2-y1-1)
else:
    print(y2-y1-1)
print(y2-y1+1)
print(y2-y1)
