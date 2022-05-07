cnt = 0
while 1:
    o, w = map(int, input().split())
    cnt += 1
    die = 0
    if o == 0 and w == 0:
        break
    else:
        while 1:
            c, n = input().split()
            if c == 'E':
                w -= int(n)
            elif c == 'F':
                w += int(n)
            elif c == '#' and n == '0':
                break
            if w <= 0:
                die += 1
        if 2*o > w > (o * 0.5) and die == 0:
            print(f"{cnt} :-)")
        elif w <= 0 or die > 0:
            print(f"{cnt} RIP")
        else:
            print(f"{cnt} :-(")
