n = float(input())
res = []
while 1:
    res.insert(0, n)
    n = float(input())
    if n == 999:
        break
    else:
        print('{:.2f}'.format(n-res.pop()))
