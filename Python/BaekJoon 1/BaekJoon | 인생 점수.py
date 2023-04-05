for _ in range(int(input())):
    r = 0
    for i in input().replace(' ',''):
        r += (ord(i)-64)
    print('PERFECT LIFE') if r == 100 else print(r)
