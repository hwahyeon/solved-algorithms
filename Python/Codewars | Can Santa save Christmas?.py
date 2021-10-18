def determine_time(arr):
    hh,mm,ss = 0,0,0
    for i in arr:
        hh += int(i.split(":")[0])
        mm += int(i.split(":")[1])
        ss += int(i.split(":")[2])
    tot = (hh*3600)+(mm*60)+ss
    if 86400 < tot:
        return False
    else:
        return True
