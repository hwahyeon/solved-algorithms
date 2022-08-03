def char_freq(message):
    dict = {}
    for i in message:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
