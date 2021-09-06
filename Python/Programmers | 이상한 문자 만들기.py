def solution(s):
    lst_str =s.split(' ')
    lst = []
    for s in lst_str:
        for n, i in enumerate(s):
            if n % 2 == 0:
                lst.append(i.upper())
            else:
                lst.append(i.lower())
        lst.append(' ')
    return ''.join(lst)[:-1]
