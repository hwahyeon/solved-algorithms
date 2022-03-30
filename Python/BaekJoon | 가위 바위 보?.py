for _ in range(int(input())):
    point1, point2 = 0, 0
    for i in range(int(input())):
        P1, P2 = input().split()
        if P1 == P2:
            point1 += 0
        elif (P1=='R' and P2=='S') or (P1=='P' and P2=='R') or (P1=='S' and P2=='P'):
            point1 += 1
        else:
            point2 += 1
    if point1 > point2:
        print('Player 1')
    elif point1 == point2:
        print("TIE")
    else:
        print('Player 2')
