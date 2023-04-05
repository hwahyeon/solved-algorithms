X1, Y1, R1 = map(int, input().split())
X2, Y2, R2 = map(int, input().split())
d = (X1-X2)**2 + (Y1-Y2)**2
print("NO") if d >= (R1+ R2) **2 else print("YES")
