def dig_pow(n, p):
    n_lst = list(map(int, str(n)))
    res = 0
    for s, i in enumerate(n_lst):
        res += (i**(s+p))
    return (res // n) if res % n == 0 else -1
