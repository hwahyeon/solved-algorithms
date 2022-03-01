def modified_sum(a, n):
    res = -1*sum(a)
    for i in a:
        res += i**n
    return res
