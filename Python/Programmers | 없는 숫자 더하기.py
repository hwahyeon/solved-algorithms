def solution(numbers):
    set_ = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    return sum(set_-set(numbers))
