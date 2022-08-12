def move_ten(st):
    a = list('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
    n = []
    for i in st:
        n.append(a.index(i)+10)
    r = ''
    for k in n:
        r += a[k]
    return r
