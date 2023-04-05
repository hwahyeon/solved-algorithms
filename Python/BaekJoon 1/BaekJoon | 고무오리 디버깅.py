Q = 0
s = input()
while 1:
    r = input()
    if r == '고무오리 디버깅 끝':
        break
    else:
        if r == '문제':
            Q += 1
        elif r == '고무오리' and Q == 0:
            Q += 2
        elif r == '고무오리':
            Q -= 1
print('고무오리야 사랑해') if Q <= 0 else print('힝구')
