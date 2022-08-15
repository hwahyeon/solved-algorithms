while 1:
    A, B, C = input().split()
    if A == '#' and B == C == '0':
        break
    else:
        if int(B) > 17 or int(C) >= 80:
            print(f'{A} Senior')
        else:
            print(f'{A} Junior')
