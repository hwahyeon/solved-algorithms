while 1:
    try:
        cnt =1
        N, M, B = map(float, input().split())
        
        while 1:
            if N * (1 + M/100) > B:
                print(cnt)
                break
            else:
                N *= (1 + M/100)
                cnt += 1
    except:
        exit()
