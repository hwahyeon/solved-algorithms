def solution(lottos, win_nums):
    dic = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    min = len(set(lottos)&set(win_nums))
    return [dic[min+lottos.count(0)], dic[min]]
