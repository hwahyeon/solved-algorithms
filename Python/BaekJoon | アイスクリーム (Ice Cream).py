S = int(input())
A = int(input())
B = int(input())
if A > S:
    print(250)
else:
    print(-(-(S-A)//B)*100 + 250)
