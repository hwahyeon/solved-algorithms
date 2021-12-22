dic = { '-':0,
        '\\':1,
        '(':2,
        '@':3,
        '?':4,
        '>':5,
        '&':6,
        '%':7,
        '/':-1}
while True:
    str_ = input()
    if str_ == '#':
        break
    else:
        res = 0
        for n, i in enumerate(str_[::-1]):
            res += 8**n * dic[i]
        print(res)
