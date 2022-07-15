def two_by_two(animals):
    if len(animals) == 0:
        return False    
    res = {}
    for i in set(animals):
        if animals.count(i) > 1:
            res[i] = 2
    return res
