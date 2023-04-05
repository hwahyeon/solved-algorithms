while 1:
    a, b, c = map(int, input().split())
    m = max(a, b, c)
    if a+b+c == 0:
        break
    elif (a**2 + b**2 + c**2) == 2*(m**2):
        print('right')
    else:
        print('wrong')
