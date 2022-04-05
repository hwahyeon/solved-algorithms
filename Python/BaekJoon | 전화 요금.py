# 1
import re

n = int(input())
won = 0
for _ in range(n):
    H, M, T = map(int, re.split('[ :]', input()))
    if H < 6:
        won += T*5
    elif 7 <= H < 18:
        won += T*10
    elif H >= 19:
        won += T*5
    elif H == 6:
        if M + T < 60:
            won += T*5
        else:
            won += (M+T-60)*10 + (60-M)*5
    elif H == 18:
        if M + T < 60:
            won += T*10
        else:
            won += (M+T-60)*5 + (60-M)*10
print(won)
