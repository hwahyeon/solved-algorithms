import re
while 1:
    s = input()
    if s == '#':
        break
    else:
        res = re.search(r'[^bdpqiovwx]+', s)
        if res:
            print("INVALID")
        else:
            tab = str.maketrans("bdpq", "dbqp")
            print(s.translate(tab)[::-1])
