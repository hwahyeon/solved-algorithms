def solution(n):
    r = 0
    for i in range(1, n+1):
        s = 0
        j = i
        while s < n:
            s += j
            j += 1
        if s == n:
            r += 1
    return r
