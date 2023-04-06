i = 1
while 1:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break

    res = (v//p) * l
    res += min((v%p), l)
    print(f'Case {i}: {res}')
    i += 1
