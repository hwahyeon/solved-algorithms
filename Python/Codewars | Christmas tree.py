def christmas_tree(height):
    total = 1 + 2*(height-1)
    res = ''
    for i in range(1, total+1):
        if i % 2 == 1:
            res += (('*'*i).center(total)+'\n')
    return res[:-1]
