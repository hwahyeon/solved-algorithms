def a(n):
    if n < 4:
        return ''
    elif n % 2 == 1:
        n = n - 1
    
    res = ' '*(n-1)+'A'+' '*(n-1)+'\n'
    s = 1
    for i in range(1, n):
        if n // 2 == i:
            res += (' '*(n-i-1)+'A '*(n//2+1)+' '*(n-i-2)+'\n')
        else:
            res += (' '*(n-i-1)+'A'+' '*s+'A'+' '*(n-i-1)+'\n')
        s += 2
    return res[:-1]
