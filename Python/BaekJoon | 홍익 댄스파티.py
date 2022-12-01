n1 = input()
n2 = input()
p = input()
n3 = input()
n4 = input()

r = ['', '', '', '', '']
for i in p:
    if i == 'm':
        r[0] += 'o'
        r[1] += 'w'
        r[2] += 'l'
        r[3] += 'n'
        r[4] += '.'
    elif i == 'l':
        r[0] += '.'
        r[1] += 'o'
        r[2] += 'm'
        r[3] += 'l'
        r[4] += 'n'
    elif i == 'o':
        r[0] += '.'
        r[1] += '.'
        r[2] += 'o'
        r[3] += 'L'
        r[4] += 'n'

for j in r:
    print(j)
