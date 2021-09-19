def solution(s):
    lst_ = ['zero','one','two','three','four','five','six','seven','eight','nine']

    for n, i in enumerate(lst_):
        s = s.replace(i, str(n))
    return int(s)
