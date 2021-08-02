def is_valid_IP(strng):
    lst = strng.split('.')
    n = 0
    for x in lst:
        if x == '0':
            pass
        elif x == '':
            n += 1
        elif x[0] == '0':
            n += 1
        elif len(lst) != 4:
            n += 1
        elif x.isnumeric() == True and 0 <= int(x) <= 255:
            pass
        else:
            n += 1
    return True if n == 0 else (False)
