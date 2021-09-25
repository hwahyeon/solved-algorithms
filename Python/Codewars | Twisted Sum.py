def compute_sum(n):
    res = 0
    for i in range(1,n+1):
        if i < 10:
            res += i
        else:
            for j in str(i):
                res += int(j)
    return res
