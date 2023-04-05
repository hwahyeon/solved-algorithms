for _ in range(int(input())):
    f = input()
    n = len(f) // 2
    if f[n-1] == f[n]:
        print('Do-it')
    else:
        print('Do-it-Not')
