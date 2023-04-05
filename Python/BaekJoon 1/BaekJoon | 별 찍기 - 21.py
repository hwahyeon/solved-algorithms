n = int(input())

if n == 1:
    print('*')
elif n % 2 == 0:
    for i in range(n):
        print('* ' * int(n/2))
        print(' *' * int(n/2))
else:
    for i in range(n):
        print('* ' * (int(n/2)+1))
        print(' *' * int(n/2))
