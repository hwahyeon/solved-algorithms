def remove_smallest(numbers):
    s = numbers[:]
    if len(s) == 0:
        return []
    s.remove(min(numbers))
    return s
