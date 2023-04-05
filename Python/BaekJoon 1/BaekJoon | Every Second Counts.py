h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
r1, r2 = (3600*h1 + 60*m1 + s1), (3600*h2 + 60*m2 + s2)

if r1 > r2:
    r2 += 24*3600

print(r2-r1)
