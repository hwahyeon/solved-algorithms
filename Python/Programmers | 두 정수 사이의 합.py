def solution(a, b):
    l = max(a, b)
    s = min(a, b)
    res = 0
    for i in range(s, l+1):
        res += i
    return res
