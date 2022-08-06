def to_weird_case(words):
    l = words.split()
    res = []
    for i in l:
        r = ''
        for n, j in enumerate(i):
            if n % 2 == 0:
                r += j.upper()
            else:
                r += j.lower()
        res.append(r)
    return ' '.join(res)
