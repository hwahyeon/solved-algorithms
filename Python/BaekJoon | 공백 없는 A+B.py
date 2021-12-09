s = input()
if len(s) == 2:
    print(int(s[0])+int(s[-1]))
elif len(s) == 4:
    print(20)
else:
    if s[:2] == '10':
        print(int(s[-1])+10)
    else:
        print(int(s[0])+10)
