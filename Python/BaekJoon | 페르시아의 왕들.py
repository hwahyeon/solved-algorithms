while 1:
    a, b, c, d = map(int, input().split())
    if a == b == c == d == 0:
        break
    else:
        print(f'{min(c, d) - max(a, b)} {max(c, d) - min(a, b)}')
