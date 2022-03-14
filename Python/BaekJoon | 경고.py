h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
ss1 = (h1 * 60 * 60) + (m1 * 60) + s1
ss2 = (h2 * 60 * 60) + (m2 * 60) + s2
if ss2 > ss1:
    res = ss2 - ss1
else:
    res = ss2 - ss1 + 24*3600

hh = res // 3600
mm = res // 60 % 60
ss = res % 60
print("%02d:%02d:%02d"%(hh,mm,ss))




# 초로 안바꾸고 풀었는데, 에러가 난다.

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
hh, mm, ss = 0, 0, 0

if s2 > s1:
    ss = s2 - s1
else:
    ss = s2 + 60 - s1
    m2 -= 1

if m2 > m1:
    mm = m2 - m1
else:
    mm = m2 +60 - m1
    h2 -= 1

if h2 > h1:
    hh = h2 - h1
else:
    hh = h2 + 24 - h1

if ss >= 60:
    ss -= 60
    mm += 1
if mm >= 60:
    mm -= 60
    hh += 1
if hh < 0:
    hh += 12

print("%02d:%02d:%02d"%(hh,mm,ss))
