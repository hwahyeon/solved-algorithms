n = int(input())
if n == 1:
    print('*')
else:
    print('*'.center(2*n-1).rstrip())
    for i in (range(2, n)):
        res = '*'+((2*i-3) * ' ')+'*'
        print( (res.center(2*n-1)).rstrip() )
    print('*'*(2*n-1))
