def starts_with(st, prefix): 
    s1 = len(st)
    s2 = len(prefix)
    if s1 < s2:
        return False
    elif st[:s2] == prefix:
        return True
    else:
        return False
