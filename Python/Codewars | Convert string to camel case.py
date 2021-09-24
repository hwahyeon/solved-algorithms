def to_camel_case(text):
    lst_ = text.replace('-',' ').replace('_',' ').split(' ')
    for i in range(1, len(lst_)):
        lst_[i] = lst_[i].capitalize()
    return ''.join(lst_)
