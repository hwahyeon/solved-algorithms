def digitize(n):
    list_dig = list(reversed(str(n)))
    res = [int(i) for i in list_dig]
    return res
