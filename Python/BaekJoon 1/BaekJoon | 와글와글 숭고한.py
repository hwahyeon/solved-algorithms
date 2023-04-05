A, B, C = map(int, input().split())
if A + B + C >= 100:
    print('OK')
else:
    if min(A, B, C) == A:
        print('Soongsil')
    elif min(A, B, C) == B:
        print('Korea')
    else:
        print('Hanyang')
