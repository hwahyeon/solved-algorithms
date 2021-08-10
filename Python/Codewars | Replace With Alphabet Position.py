def alphabet_position(text):
    text = list(filter(str.isalpha, text.upper()))
    n = 0
    for i in text:
        text[n] = ord(i) - 64
        n += 1
    res = (" ".join(map(str, text)))
    return res
