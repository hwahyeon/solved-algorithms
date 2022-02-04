def count_positives_sum_negatives(arr):
    p, m = 0, 0
    
    for i in arr:
        if i < 0:
            m += i
        elif i == 0:
            pass
        else:
            p += 1
            
    return [] if len(arr) == 0 else [p, m]
