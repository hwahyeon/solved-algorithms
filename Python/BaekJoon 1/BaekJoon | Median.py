import math

i = 1
while 1:
    l = list(map(int, input().split()))
    if l == [0]:
        break
    else:
        if l[0] % 2 == 0:
            print(f'Case {i}: {(l[int(l[0]/2)]+l[int(l[0]/2)+1])/2:.1f}')
        else:
            print(f'Case {i}: {l[math.ceil(l[0] / 2)]:.1f}')
        i += 1
