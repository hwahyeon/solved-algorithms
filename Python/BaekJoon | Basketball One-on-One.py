s = input()
A, B = 0, 0
for i in range(0, len(s), 2):
    if s[i] == 'A':
        A += int(s[i+1])
    else:
        B += int(s[i+1])
print('A') if A > B else print('B')
