r = ''
for i in range(1, int(input())+1):
    if i % 3 == 0 and i % 5 == 0:
        r += 'DeadMan' + '\n'
    elif i % 3 == 0:
        r += 'Dead' + '\n'
    elif i % 5 == 0:
        r += 'Man' + '\n'
    else:
        r += str(i) + ' '
print(r[:-1])
