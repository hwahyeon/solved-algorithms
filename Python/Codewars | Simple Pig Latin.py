def pig_it(text):
    res_lst = []
    for i in text.split(' '):
        if i != '!' and i != '?':
            res = i[1:] + i[0] + 'ay'
            res_lst.append(res)
        else:
            res_lst.append(i)
    return " ".join(res_lst)
