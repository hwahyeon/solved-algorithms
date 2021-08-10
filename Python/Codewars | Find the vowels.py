def vowel_indices(word):
    n = 1
    result = []
    for i in list(word.lower()):
        if i in {'a', 'e', 'i', 'o', 'u', 'y'}:
            result.append(n)
            n += 1
        else:
            n += 1
    return result
