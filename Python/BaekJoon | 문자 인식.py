for _ in range(int(input())):
    s = ''
    while 1:
        i = input()
        if i == '':
            break
        else:
            s += i
    res = round((len(s) - s.count('#'))/len(s)*100, 1)
    if res % 1 == 0:
        print(f'Efficiency ratio is {int(res)}%.')
    else:
        print(f'Efficiency ratio is {res}%.')
