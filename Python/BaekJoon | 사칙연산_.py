n = int(input())
for i in range(n):
    x, y = input().split(' = ')
    if eval(x) == int(y):
        print('correct')
    else:
        print('wrong answer')
