def animals(heads, legs):
    c1 = 2*heads - legs/2
    c2 = legs/2 - heads
    if int(c1) == c1 and int(c2) == c2 and c1 >= 0 and c2 >= 0:
        return (c1, c2)
    else:
        return "No solutions"
