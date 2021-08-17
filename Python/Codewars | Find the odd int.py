def find_it(seq):
    lst_ = list(set(seq))
    for i in lst_:
        if seq.count(i)%2 != 0:
            return i
