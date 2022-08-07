def add_length(str_):
    l = str_.split()
    for i in range(len(l)):
        l[i] = f'{l[i]} {str(len(l[i]))}'
    return l
