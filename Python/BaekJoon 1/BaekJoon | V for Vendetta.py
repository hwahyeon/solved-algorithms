l = list(map(int, input().split()))
for i in l:
    for n in range(i-1):
        print(' '*(n)+'*'+' '*(2*(i-n)-3)+'*')
    print(' '*(n+1)+'*')
