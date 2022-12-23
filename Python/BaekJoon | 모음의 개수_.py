import re
s = input()
print(re.sub(r'a|e|i|o|u', '*', s).count('*'))
