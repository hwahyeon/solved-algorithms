from math import pi

i = 1
while 1:
    l, r, t = map(float, input().split())
    if r == 0:
        break
    dist = (pi * l * r) / 12 / 5280
    mph = dist / t * 3600
    print(f'Trip #{i}: {dist:.2f} {mph:.2f}')
    i += 1
