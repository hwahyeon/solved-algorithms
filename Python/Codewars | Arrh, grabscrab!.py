def grabscrab(word, possible_words):
    r = []
    w = sorted(word)
    for i in possible_words:
        if sorted(i) == w:
            r.append(i)
    return r
