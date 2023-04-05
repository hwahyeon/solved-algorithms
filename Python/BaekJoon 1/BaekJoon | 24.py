h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
res = ((h2 * 3600) + (m2 * 60) + s2) - ((h1 * 3600) + (m1 * 60) + s1)
if h1 > h2:
    res += 3600 * 24
h = res//3600
m = (res % 3600)//60
s = res % 60
print(f'{h:02d}:{m:02d}:{s:02d}')
