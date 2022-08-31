def number(lines):
    r = []
    for n ,i in enumerate(lines):
        r.append(f"{n+1}: {i}")
    return r
