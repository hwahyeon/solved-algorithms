while 1:
    try:
        n, k = map(int, input().split())
        r = n
        while 1:
            if r//k == 0:
                break
            else:
                n += r//k
                r = r//k + r%k
        print(n)
    except EOFError:
        break
