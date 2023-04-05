while 1:
    A, B = map(int, input().split(' '))
    if A == B == 0:
        break
    else:
        print(2*A - B)
