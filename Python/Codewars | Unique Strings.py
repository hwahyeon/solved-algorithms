import math

def uniq_count(s):
    s = s.upper()
    l = []
    for i in set(s):
        l.append(s.count(i))
    r = 1
    for j in l:
        r *= math.factorial(j)
    return math.factorial(len(s))//r
