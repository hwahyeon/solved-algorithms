def high(x):
    list_ = x.split(' ')
    for n, i in enumerate(list_):
        c = 0
        for a in i:
            c += ord(a)-96
        list_[n] = c
    return x.split(' ')[list_.index(max(list_))]
