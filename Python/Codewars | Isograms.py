def is_isogram(string):
    str_ = string.lower()
    for i in str_:
        if str_.count(i) > 1:
            return False
    return True
