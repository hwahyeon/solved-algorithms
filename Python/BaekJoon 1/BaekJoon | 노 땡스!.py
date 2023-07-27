n = int(input())
lst = list(map(int, input().split()))

res = 0
pnt = lst[0]
pre = lst[0]

for i in lst[1:]:
    if i != pre + 1:
        res += pnt
        pnt = i
    pre = i

res += pnt
print(res)
