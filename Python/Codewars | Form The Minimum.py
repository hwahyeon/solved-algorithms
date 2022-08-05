def min_value(digits):
    res = sorted(list(set(digits)))
    return int(''.join(map(str, res)))
