n = input()
s = input()
s1, s2 = s.count('2'), s.count('e')
if s1 > s2:
    print('2')
elif s1 == s2:
    print('yee')
else:
    print('e')
