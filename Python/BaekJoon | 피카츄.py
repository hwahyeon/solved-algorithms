import re
s = input()
print('YES') if re.sub(r'pi|ka|chu', '', s) == '' else print('NO')
