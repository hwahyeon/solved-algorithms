def getCount(sentence):
    sum = 0
    for i in ['a', 'e', 'i', 'o', 'u']:
        sum += sentence.count(i)
    return sum
