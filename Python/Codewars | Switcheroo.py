def switcheroo(s):
    a = list(s)
    for n, i in enumerate(a):
        if i == 'a':
            a[n] = 'b'
        elif i == 'b':
            a[n] = 'a'
    return ''.join(a)
