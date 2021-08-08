def spin_words(sentence):
    temp_lst = sentence.split()
    for i in temp_lst:
        if len(i) > 4:
            temp_lst[temp_lst.index(i)] = i[::-1]
    res_str = " ".join(temp_lst)
    return res_str
