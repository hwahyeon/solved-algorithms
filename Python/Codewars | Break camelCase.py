def solution(s):
    lst = list(s)
    for n, i in enumerate(lst):
        if i == i.upper():
           lst[n] = ' ' + i
    return ''.join(lst)
