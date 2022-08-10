lst = list(map(int, input().split()))
lst.sort()
s = input()
r = ''
for i in s:
    if i == 'A':
        r += str(lst[0]) + ' '
    elif i == 'B':
        r += str(lst[1]) + ' '
    elif i == 'C':
        r += str(lst[2]) + ' '
print(r[:-1])
