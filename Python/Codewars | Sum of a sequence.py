def sequence_sum(begin_number, end_number, step):
    res = 0
    for i in range(begin_number, end_number+1, step):
        res += i
    return res
