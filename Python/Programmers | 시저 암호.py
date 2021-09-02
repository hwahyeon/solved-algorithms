import string

def solution(s, n):
    lower = string.ascii_lowercase*2
    upper = string.ascii_uppercase*2
    res = []
    for i in s:
        if i in lower:
            res.append(lower[lower.index(i)+n])
        elif i in upper:
            res.append(upper[upper.index(i)+n])
        else:
            res.append(' ')
    return ''.join(res)
