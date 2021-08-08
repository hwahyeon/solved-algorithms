import re

def camelize(str_):
    lst = re.sub('[^a-zA-Z0-9]',' ',str_).strip().split(' ')
    for i, n in enumerate(lst):
        lst[i] = n.capitalize()
    return "".join(lst)
