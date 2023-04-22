while 1:
    a, op, b = input().split()
    a, b =int(a), int(b)
    if a == b == 0:
        break
    if op == 'W':
        s = a - b
    else:
        s = a + b
    if s < -200:
        print('Not allowed')
    else:
        print(s)
