l = input().split()

def eq(a, b, op):
    if(op == '+'): return a + b
    if(op == '-'): return a - b
    if(op == '*'): return a * b
    return -1*(abs(a)//abs(b)) if a*b < 0 else a//b

x, y, z = int(l[0]), int(l[2]), int(l[4])
op1, op2 = l[1], l[3]

r1 = eq(eq(x, y, op1), z, op2)
r2 = eq(x, eq(y, z, op2), op1)

print(min(r1, r2))
print(max(r1, r2))
