def sum_two_smallest_numbers(numbers):
    n = sorted(numbers)
    return sum(n[:2])
