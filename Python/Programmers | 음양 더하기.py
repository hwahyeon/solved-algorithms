def solution(absolutes, signs):
    for n, i in enumerate(signs):
        if i == True:
            signs[n] = 1
        else:
            signs[n] = -1
    return sum([x*y for x,y in zip(absolutes,signs)])
