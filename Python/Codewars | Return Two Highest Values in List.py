def two_highest(arg1):
    if len(set(arg1)) < 2:
        return arg1
    else:
        return sorted(set(arg1), reverse=True)[0:2]
