def to_acronym(inp):
    r = ''
    for i in list(inp.split()):
        r += i[0]
    return r.upper()
