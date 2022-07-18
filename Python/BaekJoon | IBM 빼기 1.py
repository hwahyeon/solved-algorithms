for s in range(int(input())):
    res = ''
    for i in input():
        if i == 'Z':
            res += 'A'
        else:
            res += chr(ord(i)+1)
    print(f'String #{s+1}')
    print(res)
    print()
