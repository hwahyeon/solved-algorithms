n = int(input())
print('*'*n+' '*(2*(n-1)-1)+'*'*n)
s = '*'+' '*(n-2)+'*'
m = ' '*(n-1) + ('*'+' '*(n-2)+'*'+' '*(n-2)+'*')
space = 2*n-3
for i in range(1, n-1):
    space -= 2
    print(' '*i+s+(' '*(space))+s)
print(m)
for i in reversed(range(1, n-1)):
    print(' '*i+s+(' '*(space))+s)
    space += 2
print('*'*n+' '*(2*(n-1)-1)+'*'*n)
