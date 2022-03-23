for _ in range(int(input())):
    n = int(input())
    for s, i in enumerate(format(n, 'b')[::-1]):
        if i == '1':
            print(s, end=' ')
