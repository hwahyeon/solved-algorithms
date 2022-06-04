def remove(s):
    while 1:
        if s[-1] != '!':
            break
        else:
            s = s[:-1]
    return s
