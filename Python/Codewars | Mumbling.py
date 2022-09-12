def accum(s):
    l = []
    for n, i in enumerate(s.lower()):
        l.append(i.upper()+i*(n))
    return '-'.join(l)
