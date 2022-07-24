def find_most_frequent(l):
    m = 0
    r = []
    for i in l:
        if m <= l.count(i):
            m = l.count(i)
            r.append(i)
    return set(r)
