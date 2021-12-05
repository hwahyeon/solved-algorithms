def x(n):
    res = []
    a, b = 0, -1
    for i in range(n):
        lst = [0]*n
        lst[a], lst[b] = 1, 1
        res.append(lst)
        a += 1
        b -= 1
    return res
