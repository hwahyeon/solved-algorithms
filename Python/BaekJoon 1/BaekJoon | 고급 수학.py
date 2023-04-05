for i in range(int(input())):
    print(f'Scenario #{i+1}:')
    a, b, c = map(int, input().split())
    a1, b1, c1 = a**2, b**2, c**2
    if 2*max(a1, b1, c1) - (a1 + b1 + c1) == 0:
        print('yes\n')
    else:
        print('no\n')
