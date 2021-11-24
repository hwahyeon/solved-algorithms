N = input()
cnt = 0
for i in N:
    if i in ('ABC'):
        cnt += 3
    elif i in ('DEF'):
        cnt += 4
    elif i in ('GHI'):
        cnt += 5
    elif i in ('JKL'):
        cnt += 6
    elif i in ('MNO'):
        cnt += 7
    elif i in ('PQRS'):
        cnt += 8
    elif i in ('TUV'):
        cnt += 9
    elif i in ('WXYZ'):
        cnt += 10
print(cnt)
