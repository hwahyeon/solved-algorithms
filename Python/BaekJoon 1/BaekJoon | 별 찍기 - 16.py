n = int(input())
for i in range(n):
    print((('*' + ' *'*i).center(2*n-1)).rstrip())
