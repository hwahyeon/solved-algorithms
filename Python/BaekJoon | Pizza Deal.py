from math import pi

A1, P1 = map(int, input().split())
R1, P2 = map(int, input().split())

print("Slice of pizza") if P1/A1 < P2/(pi*(R1**2)) else print("Whole pizza")
