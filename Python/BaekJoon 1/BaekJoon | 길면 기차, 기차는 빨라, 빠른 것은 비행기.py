while 1:    
    M, A, B = map(int, input().split())
    if M == A == B == 0:
        break
    tot = round((M/A - M/B) * 3600)
    
    h = tot//3600
    m = (tot%3600)//60
    s = tot%60

    print(f"{h}:{m:02d}:{s:02d}")
