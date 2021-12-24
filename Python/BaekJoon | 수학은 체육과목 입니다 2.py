n=int(input())
if n<6:
    print(n)
else:
    print([2,1,2,3,4,5,4,3][n%8])
