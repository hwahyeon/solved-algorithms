import re
n = int(input())
s = input().lower()
print(len(re.sub(r'[^aeiou]', '', s)))
