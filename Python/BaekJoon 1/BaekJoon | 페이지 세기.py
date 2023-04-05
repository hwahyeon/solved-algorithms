while 1:
    n = int(input())
    if n == 0:
        break
    else:
        s1 = set()
        d = list(input().split(','))
        for i in d:
            if '-' in i:
                a, b = map(int, i.split('-'))
                if a <= b and a <= n:
                    if b <= n:
                        for j in range(a, b + 1):
                            s1.add(j)
                    else:
                        for j in range(a, n + 1):
                            s1.add(j)
            else:
                if int(i) <= n:
                    s1.add(int(i))
    print(len(s1 - {0}))
