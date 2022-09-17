import re

def stock_list(listOfArt, listOfCat):
    r = []
    e = 0
    for i in listOfCat:
        s = 0
        for j in listOfArt:
            if i == j[0]:
                s += int(re.sub(r'[^0-9]', '', j))
        e += s
        r.append(f'({i} : {s})')
    return ' - '.join(r) if e != 0 else ""
