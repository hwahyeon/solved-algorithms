def ordered_count(inp):
    res = []
    check = ''
    for i in inp:
        if i not in check:
            check += i
            res.append((i, inp.count(i)))
    return res
