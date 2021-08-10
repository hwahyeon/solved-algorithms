def correctness(bob, expe): 
    Point = 0
    for i in range(len(bob)):
        if bob[i]==expe[i]:
            Point += 1
        elif bob[i]=='?' or expe[i]=='?':
            Point += 0.5
    return Point
