def sum(*args):
    res = 0
    for i in args:
        if type(i) is int:
            res += i
    return res
