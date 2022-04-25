def give_change(amount): 
    res = []
    for i in [100, 50, 20, 10, 5, 1]:
        res.insert(0, amount // i)
        amount %= i
    return tuple(res)
