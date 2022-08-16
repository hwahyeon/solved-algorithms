def longest(a1, a2):
    s = list(set(a1 + a2))
    s.sort()
    return ''.join(s)
