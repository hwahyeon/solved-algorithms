def multiplication_table(size):
    r = []
    l1 = []
    for i in range(1, size+1):
        l1.append(i)
    for j in range(1, size+1):
        l2 = []
        for k in l1:
            l2.append(j*k)
        r.append(l2)
    return r
