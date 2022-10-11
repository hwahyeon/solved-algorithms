def clean_string(s):
    r = ''
    for i in s:
        if i == '#':
            r = r[:-1]
        else:
            r += i
    return r
