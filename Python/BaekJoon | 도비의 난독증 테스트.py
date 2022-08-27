while 1:
    ori = []
    res = []
    n = int(input())
    if n == 0:
        break
    else:
        for _ in range(n):
            s = input()
            ori.append(s)
            res.append(s.lower())
        print(ori[res.index(min(res))])
