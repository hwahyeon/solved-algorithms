# 시간초과
for _ in range(3):
    sum = 0
    n = int(input())
    for i in range(n):
        sum += int(input())
    if sum == 0:
        print(0)
    elif sum > 0:
        print('+')
    else:
        print('-')


# 수정
from sys import stdin

for _ in range(3):
    sum = 0
    n = int(stdin.readline())
    for i in range(n):
        sum += int(stdin.readline())
    if sum == 0:
        print(0)
    elif sum > 0:
        print('+')
    else:
        print('-')
