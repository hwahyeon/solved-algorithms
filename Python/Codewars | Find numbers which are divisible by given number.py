def divisible_by(numbers, divisor):
    r = []
    for i in numbers:
        if i % divisor == 0:
            r.append(i)
    return r
