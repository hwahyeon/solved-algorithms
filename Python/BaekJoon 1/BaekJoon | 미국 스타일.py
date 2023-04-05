for _ in range(int(input())):
    a, b = input().split()
    if b == 'kg':
        print(f'{float(a)*2.2046:.4f} lb')
    elif b == 'g':
        print(f'{float(a)*3.7854:.4f} l')
    elif b == 'l':
        print(f'{float(a)*0.2642:.4f} g')
    elif b == 'lb':
        print(f'{float(a)*0.4536:.4f} kg')
