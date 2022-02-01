l = ['o', 'x', 'x']
for i in input():
    if i == 'A':
        l[0], l[1] = l[1], l[0]
    elif i == 'B':
        l[1], l[2] = l[2], l[1]
    else:
        l[0], l[2] = l[2], l[0]

print(l.index('o')+1)
