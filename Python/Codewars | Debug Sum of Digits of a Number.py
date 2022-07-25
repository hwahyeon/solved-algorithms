def get_sum_of_digits(num):
    res = 0
    for i in str(num):
        res += int(i)
    return res
