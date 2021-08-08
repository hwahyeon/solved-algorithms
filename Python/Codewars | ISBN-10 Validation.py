def valid_ISBN10(isbn):
    res = 0
    if len(isbn) != 10:
        return False
    elif isbn.isdigit() == True:
        for n, i in enumerate(isbn):
            res += ((n + 1) * int(i))
        return True if res % 11 == 0 else False
    elif isbn[:-2].isdigit() and isbn[-1] == 'X':
        for n, i in enumerate(isbn[:-1]):
            res += ((n + 1) * int(i))
        return True if (res + 100) % 11 == 0 else False
    else:
        return False
