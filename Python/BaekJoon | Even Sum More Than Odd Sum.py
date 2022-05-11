for _ in range(int(input())):
    odd, even = 0, 0
    for i in list(map(int, input().split()))[1:]:
        if i % 2 == 0:
            even += i
        else:
            odd += i

    if odd > even:
        print('ODD')
    elif odd < even:
        print('EVEN')
    else:
        print('TIE')
