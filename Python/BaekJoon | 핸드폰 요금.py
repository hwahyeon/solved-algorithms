n = input()
lst = list(map(int, input().split()))

won1, won2 = 0, 0
for i in lst:
    won1 += i//30 * 10 + 10
    won2 += i//60 * 15 + 15

if won1 == won2:
    print('Y M', won1)
elif won1 < won2:
    print('Y', won1)
else:
    print('M', won2)
