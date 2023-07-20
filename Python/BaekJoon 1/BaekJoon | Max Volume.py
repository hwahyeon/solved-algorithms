res = 0
pi = 3.14159
for _ in range(int(input())):
    l = list(input().split())
    r = float(l[1])
    h = float(l[2]) if len(l) > 2 else 0
    
    if l[0] == 'C':
        t = (1/3) * pi * (r ** 2) * h
    elif l[0] == 'L':
        t = pi * (r ** 2) * h
    elif l[0] == 'S':
        t = (4/3) * pi * (r ** 3)
        
    if t >= res:
        res = t
print(f"{res:.3f}")
