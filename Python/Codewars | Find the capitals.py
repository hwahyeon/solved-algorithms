def capitals(word):
    res = []
    for n, i in enumerate(list(word)):
        if i.isupper():
            res.append(n)
    return res
