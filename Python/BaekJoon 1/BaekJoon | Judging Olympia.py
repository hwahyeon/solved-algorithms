while 1:
    s = input()
    if s == '0 0 0 0 0 0':
        break
    else:
        l = sorted(list(map(int, s.split())))
        r = sum(l[1:-1])/4
        if int(r) == r:
            print(int(r))
        else:
            print(r)
