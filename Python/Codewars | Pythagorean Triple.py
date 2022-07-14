def pythagorean_triple(integers):
    l = sorted(integers)
    return l[0]**2 + l[1]**2 == l[2]**2
