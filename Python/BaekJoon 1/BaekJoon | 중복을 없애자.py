while 1:
    l = list(map(int, input().split()))
    if l == [0]:
        break
    else:
        r = ''
        for i in range(1, len(l)):
            if l[i] != l[i-1]:
                r += str(l[i]) + ' '
        print(f"{r}$")
