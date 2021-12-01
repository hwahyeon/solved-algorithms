def f(n, m):
    t = (int((m-1)*m/2))*(n//m)
    s = n%m+1
    t += int((s-1)*s/2)
    return t
