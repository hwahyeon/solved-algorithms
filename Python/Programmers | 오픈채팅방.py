def solution(record):
    dic = {}
    res = []
    for i in record:
        try:
            a, b, c = i.split(' ')
            dic[b] = c
        except:
            a, b = i.split(' ')

    for i in record:
        try:
            a, b, c = i.split(' ')
        except:
            a, b = i.split(' ')
        if a == 'Enter':
            res.append(dic[b]+'님이 들어왔습니다.')
        elif a == 'Leave':
            res.append(dic[b]+'님이 나갔습니다.')
    return res
