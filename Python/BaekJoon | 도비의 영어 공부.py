while 1:
    l = list(input().lower().split())
    if l[0] == '#':
        break
    else:
        res = 0
        for i in l[1:]:
            res += i.count(l[0])
        print(f'{l[0]} {res}')
