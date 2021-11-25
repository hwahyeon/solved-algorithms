def uni_total(s):
    res = 0
    for i in s:
        res += int(ord(i))
    return res
