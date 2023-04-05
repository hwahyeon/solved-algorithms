import re

def CtoP(t):
    return t[0].upper() + t[1:]

def PtoC(t):
    return t[0].lower() + t[1:]

def StoP(t):
    l = t.split('_')
    for i in range(len(l)):
        l[i] = CtoP(l[i])
    return ''.join(l)

def PtoS(t):
    r = t[1:]
    c = re.compile('[A-Z]')
    for i in c.findall(t):
        r = r.replace(i, '_'+i.lower())
    return t[0].lower() + r

n, s = input().split()

if n == '1':
    print(s)
    print(PtoS(s))
    print(CtoP(s))
elif n == '2':
    print(PtoC(StoP(s)))
    print(s)
    print(StoP(s))
elif n == '3':
    print(PtoC(s))
    print(PtoS(s))
    print(s)
