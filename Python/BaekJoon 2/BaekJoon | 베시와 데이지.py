B1, B2 = map(int, input().split())
D1, D2 = map(int, input().split())
J1, J2 = map(int, input().split())

B = max(abs(J1-B1), abs(J2-B2))
D = abs(J1-D1) + abs(J2-D2)

if B > D:
    print("daisy")
elif B < D:
    print("bessie")
else:
    print("tie")
