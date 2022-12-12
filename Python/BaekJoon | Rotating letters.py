import re
s = input()
print('YES') if re.sub(r'I|O|S|H|Z|X|N', '', s) == '' else print('NO')
