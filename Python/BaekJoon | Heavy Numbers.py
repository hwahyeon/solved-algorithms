a, b = input().split()

def heavy_num(n):
    c = 0
    for i in n:
        c += int(i)
    return len(n)*c

if heavy_num(a) > heavy_num(b):
    print(1)
elif heavy_num(a) < heavy_num(b):
    print(2)
else:
    print(0)
