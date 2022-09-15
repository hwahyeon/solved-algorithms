def pattern(n):
    r = ''
    if n < 1:
        return r
    for i in range(1, n+1):
        r += (f'{i}'*i+f'\n')
    return r[:-1]
