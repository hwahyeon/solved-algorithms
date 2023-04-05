while 1:
    res = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    sen = input().lower()
    if sen == '#':
        break
    else:
        for i in vowel:
            res += sen.count(i)
    print(res)
