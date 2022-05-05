def to_jaden_case(string):
    lst = string.split()
    for n, i in enumerate(lst):
        lst[n] = i.capitalize()
    return ' '.join(lst)
