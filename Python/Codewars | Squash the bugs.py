def find_longest(string):
    spl = string.split(' ')
    res = 0
    for i in range(len(spl)):
        if len(spl[i]) > res:
            res = len(spl[i])
    return res
