lst = [int(input()) for i in range(9)]
tot = sum(lst)
for n, i in enumerate(lst):
    for j in lst[n+1:]:
        if 100 == tot-(i+j):
            t1, t2 = i, j
lst.remove(t1)
lst.remove(t2)
res = sorted(lst)

for l in res:
    print(l)
