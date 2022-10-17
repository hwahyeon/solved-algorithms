def sum_no_duplicates(l):
    r = 0
    for i in set(l):
        if l.count(i) < 2:
            r += i
    return r
