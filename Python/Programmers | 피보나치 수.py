def solution(n):
    before, after = 0, 1
    for i in range(n):
        before, after = after, before + after
    return before%1234567
