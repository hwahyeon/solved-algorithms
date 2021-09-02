def solution(n):
    rev = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rev += str(mod)
    return int(rev, 3)
