def solution(number):
    res = 0
    for i in range(number-1):
        if (i+1) % 3 == 0 or (i+1) % 5 == 0:
            res += (i+1)
    return res if res > 0 else 0
