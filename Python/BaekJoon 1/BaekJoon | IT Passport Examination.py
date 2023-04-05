for _ in range(int(input())):
    no, L1, L2, L3 = map(int, input().split())
    sum = L1 + L2 + L3
    if sum < 54:
        res = 'FAIL'
    elif L1 < 35*0.3 or L2 < 25*0.3 or L3 < 40*0.3:
        res = 'FAIL'
    else:
        res = 'PASS'
    print('{} {} {}'.format(no, sum, res))
