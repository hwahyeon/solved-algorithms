def max_tri_sum(numbers):
    n = sorted(set(numbers))
    return sum(n[-3:])
