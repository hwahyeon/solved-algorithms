def each_cons(lst, n):
    res = []
    t = len(lst) - n + 1
    for i in range(t):
        res.append(lst[i:n+i])
    return res
