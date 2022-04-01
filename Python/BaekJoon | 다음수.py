while 1:
    A, B, C = map(int, input().split())
    if A == B == C == 0:
        break
    elif B - A == C - B:
        print('AP', C + B - A)
    else:
        print('GP', C * (B // A))
