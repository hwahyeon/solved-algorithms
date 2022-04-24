while 1:
    n = input()
    if n == '0':
        break
    else:
        print('yes') if n[::-1] == n else print('no')
