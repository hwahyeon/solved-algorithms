n = int(input())
if n == 1:
    print('*')
elif n % 2 == 0:
    for i in range(int(n/2)):
        print('* ' * n)
        print(' *' * n)
else:
    for i in range(int(n/2)):
        print('* ' * n)
        print(' *' * n)
    print('* ' * n)
