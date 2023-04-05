A, B = 0, 0
A += int(input())*3 + int(input())*2 + int(input())
B += int(input())*3 + int(input())*2 + int(input())

if A == B:
    print("T")
elif A > B:
    print("A")
else:
    print("B")
