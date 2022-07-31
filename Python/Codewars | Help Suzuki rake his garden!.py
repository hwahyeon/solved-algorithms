def rake_garden(garden):
    l = garden.split()
    for n, i in enumerate(l):
        if i != 'gravel' and i != 'rock':
            l[n] = 'gravel'
    return ' '.join(l)
