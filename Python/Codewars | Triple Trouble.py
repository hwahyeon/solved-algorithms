def triple_trouble(one, two, three):
    res = ''
    for i in range(len(one)):
        res += one[i]
        res += two[i]
        res += three[i]
    return res
