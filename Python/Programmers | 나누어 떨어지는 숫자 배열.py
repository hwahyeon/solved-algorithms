def solution(arr, divisor):
    res = []
    for i in arr:
        if i%divisor == 0:
            res.append(i)
    return sorted(res) if len(res)>0 else [-1]
