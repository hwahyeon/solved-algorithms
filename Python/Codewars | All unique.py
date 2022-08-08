def has_unique_chars(string):
    l = list(string)
    return len(l) == len(set(l))
