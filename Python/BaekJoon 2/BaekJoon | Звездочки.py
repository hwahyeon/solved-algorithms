for i in range(1, int(input()) + 1):
    n = i**2
    if n > 100:
        print('*'*100+'...')
    else:
        print('*'*n)
