def likes(names):
    nolst = len(names)
    if nolst == 0:
        r = 'no one likes this'
    elif nolst == 1:
        r = names[0] + ' likes this'
    elif nolst == 2:
        r = names[0] + ' and ' + names[1] + ' like this'
    elif nolst == 3:
        r = names[0] + ', '+ names[1] + ' and ' + names[2] + ' like this'
    else:
        r = names[0] + ', '+ names[1] + ' and ' + str(nolst-2) + ' others like this'
    return r
