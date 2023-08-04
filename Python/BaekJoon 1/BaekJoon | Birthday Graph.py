j = 1
while 1:
    n = int(input())
    if n == 0:
        break
    else:
        b = [0] * 12
        m = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

        for _ in range(n):
            dd, mm, yyyy = map(int, input().split())
            b[mm-1] += 1
        
        print(f'Case #{j}:')
        for i in range(12):
            print(f'{m[i]}:{"*"*b[i]}')
        j += 1
