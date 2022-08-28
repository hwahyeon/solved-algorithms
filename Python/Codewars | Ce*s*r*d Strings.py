def uncensor(infected, discovered):
    lst = list(infected)
    n = 0
    for s, i in enumerate(lst):
        if i == '*':
            lst[s] = discovered[n]
            n += 1
    return ''.join(lst)
