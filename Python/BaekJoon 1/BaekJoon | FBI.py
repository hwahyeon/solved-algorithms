c = ''
for i in range(1, 6):
    n = input()
    if "FBI" in n:
        c += str(i) + ' '
print(c[:-1]) if c != '' else print('HE GOT AWAY!')
