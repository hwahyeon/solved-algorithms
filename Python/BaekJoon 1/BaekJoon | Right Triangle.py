for i in range(int(input())):
    a, b, c = map(int, input().split())
    a, b, c = a**2, b**2, c**2
    if a == b + c or b == a + c or c == a + b:
        r = 'YES'
    else:
        r = 'NO'
    print(f'Case #{i+1}: {r}')
