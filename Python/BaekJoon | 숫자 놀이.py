while 1:
    n = sum(list(map(int, input())))
    if n == 0:
        break
    else:
        while 1:
            if n < 10:
                print(n)
                break
            else:
                n = sum(list(map(int, str(n))))
