while 1:
    s = input()
    if s == '*':
        break
    else:
        if len(list(set(s.replace(' ','')))) > 25:
            print('Y')
        else:
            print('N')
