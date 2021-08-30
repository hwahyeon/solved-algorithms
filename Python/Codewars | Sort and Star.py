def two_sort(array):
    array.sort()
    res_ = []
    [res_.extend([i, '***']) for i in array[0]]
    return ''.join(res_[:-1])
