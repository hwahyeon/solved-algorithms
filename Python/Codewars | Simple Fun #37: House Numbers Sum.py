def house_numbers_sum(inp):
    r = 0
    for i in inp:
        if i != 0:
            r += i
        else:
            break
    return r
