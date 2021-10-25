def nth_char(words):
    res = []
    for n, i in enumerate(words):
        res.append(i[n])
    return ''.join(res)
