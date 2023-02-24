n = input()
s = input()
if s.count('e') == s.count('g'):
    print('bigdata? security!')
elif s.count('e') > s.count('g'):
    print('security!')
else:
    print('bigdata?')
