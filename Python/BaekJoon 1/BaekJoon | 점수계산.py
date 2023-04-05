n = input()
ox = list(map(int, input().split()))

extra = 0
res = 0
for i in ox:
    if i == 0:
        extra = 0
    else:
        extra += 1
        res += extra
print(res)
