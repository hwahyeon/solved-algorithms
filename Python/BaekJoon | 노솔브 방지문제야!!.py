import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = int(bin(n)[2:])
    if a&(-a) == n:
        print(1)
    else:
        print(0)
