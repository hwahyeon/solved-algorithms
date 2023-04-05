tri = [int(input()) for i in range(3)]

if sum(tri) == 180:
    if tri.count(60) == 3:
        print('Equilateral')
    elif tri.count(tri[0]) == 2 or tri.count(tri[2]) == 2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')
