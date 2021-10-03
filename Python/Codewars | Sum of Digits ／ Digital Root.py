def digital_root(n):
    while len(str(n))>1:
        res = 0
        for i in str(n):
            res += int(i)
        n = res
    return n
