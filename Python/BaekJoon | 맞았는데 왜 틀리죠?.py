S1, S2 = map(int, input().split())
t1, t2 = 0, 0
for i in range(S1):
    a, b = map(int, input().split())
    if a != b:
        t1 += 1
for j in range(S2):
    a, b = map(int, input().split())
    if a != b:
        t2 += 1
if t1 != 0:
    print("Wrong Answer")
elif t2 != 0:
    print("Why Wrong!!!")
else:
    print("Accepted")
