def reverse_words(text):
    lst_ = text.split(' ')
    for n, i in enumerate(lst_):
        lst_[n] = i[::-1]
    return " ".join(lst_)
