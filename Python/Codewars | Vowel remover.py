def shortcut( s ):
    for i in ['a', 'e', 'i', 'o', 'u']:
        s = s.replace(i, '')
    return s
