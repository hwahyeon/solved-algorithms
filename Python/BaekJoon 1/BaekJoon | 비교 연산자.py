i = 1
while 1:
    l = list(input().split())
    if l[1] == 'E':
        break
    else:
        r = 'true' if eval(' '.join(l)) else 'false'
        print(f'Case {i}: {r}')
        i += 1
