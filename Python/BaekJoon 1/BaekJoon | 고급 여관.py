A_a, A_h = map(int, input().split())
B_a, B_h = map(int, input().split())

while 1:
    if A_h <= 0 or B_h <= 0:
        break
    else:
        A_h -= B_a
        B_h -= A_a

if A_h <= 0 and B_h <= 0:
    print('DRAW')
elif A_h <= 0 and B_h >0:
    print('PLAYER B')
elif B_h <= 0 and A_h >0:
    print('PLAYER A')
