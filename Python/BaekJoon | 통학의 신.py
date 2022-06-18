A, B = map(int, input().split())
A *= 2
D = (A**2) - (4*B)
if D > 0:
    r1 = (-A + (A**2 - 4*B)**0.5)/(2)
    r2 = (-A - (A**2 - 4*B)**0.5)/(2)
    print(int(min(r1,r2)), int(max(r1,r2)))
elif D == 0:
    print(int(-A / 2))
