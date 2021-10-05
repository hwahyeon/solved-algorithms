n, max = map(int, input().split())
lst_ = list(map(int, input().split()))
res = []
for i in lst_:
    if i < max:
        res.append(str(i))
print(' '.join(res))
