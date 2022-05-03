def bingo(array): 
    cnt = 0
    for i in [2, 7, 9, 14, 15]:
        if i in array:
            cnt += 1
    return 'WIN' if cnt >= 5 else 'LOSE'
