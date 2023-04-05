for _ in range(int(input())):
    coin = input()
    r = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, len(coin)):
        s = coin[i:i+3]
        if s == 'TTT':
            r[0] += 1
        elif s == 'TTH':
            r[1] += 1
        elif s == 'THT':
            r[2] += 1
        elif s == 'THH':
            r[3] += 1
        elif s == 'HTT':
            r[4] += 1
        elif s == 'HTH':
            r[5] += 1
        elif s == 'HHT':
            r[6] += 1
        elif s == 'HHH':
            r[7] += 1
    print(*r)
