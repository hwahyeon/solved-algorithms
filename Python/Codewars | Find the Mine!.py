def mineLocation(field):
    r = 0
    res = []
    for i in field:
        if 1 in i:
            res.append(r)
            res.append(i.index(1))
            r += 1
        else:
            r += 1
    return res
