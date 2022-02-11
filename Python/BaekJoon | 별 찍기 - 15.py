n = int(input())
print('*'.center(2*n-1).rstrip())
for i in (range(2, n+1)):
    res = '*'+((2*i-3) * ' ')+'*'
    print( (res.center(2*n-1)).rstrip() )
