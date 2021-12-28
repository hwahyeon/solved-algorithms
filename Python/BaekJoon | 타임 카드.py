for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    res = (h2*3600 + m2*60 + s2) - (h1*3600 + m1*60 + s1)
    
    h, r = divmod(res, 3600)
    m, s = divmod(r, 60)
    print(h,m,s)
