while 1:
    try:
        n, s = map(int, input().split())
        print(int(s / (n + 1)))
    except EOFError:
        break
