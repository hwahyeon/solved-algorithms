def generate_range(min, max, step):
    res = []
    for i in range(min, max+1, step):
        res.append(i)
    return res
