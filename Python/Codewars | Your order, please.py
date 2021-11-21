import re

def order(sentence):
    lst1 = list(sentence.split())
    lst2 = list(sentence.split())
    res = []

    for i in lst1:
      num = re.sub(r'[^0-9]', '', i)
      lst2[int(num)-1] = i
    
    return ' '.join(lst2)
