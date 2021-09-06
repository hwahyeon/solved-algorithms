def solution(num):
    res = 0
    while res<501:
        if num%2 == 0:
            num = num/2
            res += 1
        elif num == 1:
            break
        else:
            num = (num * 3) + 1
            res += 1
    return res if res < 501 else -1
