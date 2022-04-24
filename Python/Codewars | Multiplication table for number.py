def multi_table(number):
    res = ''
    for i in range(1, 11):
        res += f'{i} * {number} = {i * number}\n'
    return res[:-1]
