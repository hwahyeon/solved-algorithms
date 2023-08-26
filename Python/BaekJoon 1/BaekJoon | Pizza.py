import math

for _ in range(int(input())):
    A1, P1 = map(int, input().split())
    R1, P2 = map(int, input().split())
    
    value_slice = A1 / P1

    value_whole = (math.pi * R1**2) / P2

    if value_slice > value_whole:
        print("Slice of pizza")
    else:
        print("Whole pizza")
