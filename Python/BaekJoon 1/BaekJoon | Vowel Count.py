import re

for _ in range(int(input())):
    s = input()
    r = re.sub(r'[aeiou]', '*', s).count('*')
    
    print(s)
    if r > len(s) - r:
        print(1)
    else:
        print(0)
