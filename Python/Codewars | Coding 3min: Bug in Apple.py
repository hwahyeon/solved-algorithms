def sc(apple):
    for n, i in enumerate(apple):
        if 'B' in i:
            return [n, i.index("B")]
