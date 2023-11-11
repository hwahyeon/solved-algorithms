while 1:
    s = int(input())
    if s == 0:
        break
    else:
        if s % 42 == 0:
            print('PREMIADO')
        else:
            print('TENTE NOVAMENTE')
