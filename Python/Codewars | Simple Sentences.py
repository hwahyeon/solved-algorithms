def make_sentences(parts):
    remove_set = {'.'}
    lst = [i for i in parts if i not in remove_set]
    return ' '.join(lst).replace(' ,',',') + '.'
