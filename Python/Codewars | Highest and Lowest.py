def high_and_low(numbers):
    res_ = [int(i) for i in numbers.split(' ')]
    return "{} {}".format(max(res_), min(res_))
