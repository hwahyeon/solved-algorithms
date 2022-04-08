def remove_every_other(my_list):
    res = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            res.append(my_list[i])
    return res
