def computer_to_phone(numbers):
    lst_ = list(map(int, list(numbers)))
    for n, i in enumerate(lst_):
        if i > 6:
            lst_[n] = i-6
        elif i < 4 and i > 0:
            lst_[n] = i+6
    return ''.join(map(str, lst_))
