for i in range(int(input())):
    a1, b1, c1, d1, e1, f1 = map(int, input().split())
    a2, b2, c2, d2, e2, f2, g2 = map(int, input().split())
    res1 = a1 + 2*b1 + 3*c1 + 3*d1 + 4*e1 + 10*f1
    res2 = a2 + 2*b2 + 2*c2 + 2*d2 + 3*e2 + 5*f2 + 10*g2
    if res1 > res2:
        res = "Good triumphs over Evil"
    elif res1 == res2:
        res = "No victor on this battle field"
    else:
        res = "Evil eradicates all trace of Good"
    print(f'Battle {i+1}: {res}')
