for _ in range(int(input())):
    s = input()
    n = int(len(s)**0.5)
    l = []
    for i in range(n):
        l.append(list(s[i*n:(i+1)*n]))
    
    res = ''
    for j in range(n):
        for k in range(n):
            res += l[n-1-k][j]
    print(res[::-1])
