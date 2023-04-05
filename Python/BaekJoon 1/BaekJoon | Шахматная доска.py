n = int(input())

if n < 9:
    print(['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'][n-1])
elif n%8 == 0:
    print('h' + str(n//8))
else:
    print(['h', 'a', 'b', 'c', 'd', 'e', 'f', 'g'][n%8] + str(n//8+1))
