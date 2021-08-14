num = int(input())

for i in range(1, num):
    print('*'*i + ' '*2*(num-i) + '*'*i)
for i in range(num, 0, -1):
    print('*'*i + ' '*2*(num-i) + '*'*i)
