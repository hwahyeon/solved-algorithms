def gordon(a):
    l = list(a.upper().split())
    for i in range(len(l)):
        l[i] += '!!!!'
    r = ' '.join(l)    
    
    tab = str.maketrans(
        "AEIOU",
        "@****")
    return r.translate(tab)
