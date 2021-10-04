def duplicate_count(text):
    lst_ = list(text.lower())
    set_ = set(lst_)
    res = 0
    for i in set_:
        if lst_.count(i) > 1:
            res += 1
    return res
