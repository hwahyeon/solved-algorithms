def largest_pair_sum(numbers):
    n = sorted(numbers)
    return n[-1] + n[-2]
