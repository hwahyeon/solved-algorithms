l = list(map(int, input().split()))
x, y, r = map(int, input().split())
if x in l:
    print(l.index(x) + 1)
else:
    print(0)
