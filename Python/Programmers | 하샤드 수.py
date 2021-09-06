def solution(x):
    s = 0
    for i in str(x):
        s += int(i)
    return True if x%s==0 else False
