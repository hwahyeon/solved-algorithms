num = input()

for n in range(len(num)):
    i = int(num[n])
    if i == 0:
        print('0000')
        print('0  0')
        print('0  0')
        print('0  0')
        print('0000')
    elif i == 1:
        print('   1')
        print('   1')
        print('   1')
        print('   1')
        print('   1')
    elif i == 2:
        print('2222')
        print('   2')
        print('2222')
        print('2')
        print('2222')
    elif i == 3:
        print('3333')
        print('   3')
        print('3333')
        print('   3')
        print('3333')
    elif i == 4:
        print('4  4')
        print('4  4')
        print('4444')
        print('   4')
        print('   4')
    elif i == 5:
        print('5555')
        print('5')
        print('5555')
        print('   5')
        print('5555')
    elif i == 6:
        print('6666')
        print('6')
        print('6666')
        print('6  6')
        print('6666')
    elif i == 7:
        print('7777')
        print('   7')
        print('   7')
        print('   7')
        print('   7')
    elif i == 8:
        print('8888')
        print('8  8')
        print('8888')
        print('8  8')
        print('8888')
    elif i == 9:
        print('9999')
        print('9  9')
        print('9999')
        print('   9')
        print('   9')

    if n+1 != len(num):
        print()
