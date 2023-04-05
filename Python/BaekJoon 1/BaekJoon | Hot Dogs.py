while 1:
    try:
        H, P = map(int, input().split())
        print('{:.2f}'.format(H/P))
    except EOFError:
        break
