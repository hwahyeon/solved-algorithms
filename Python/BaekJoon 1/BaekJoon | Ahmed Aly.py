for i in range(int(input())):
    eq, r = input().split('=')
    ans = 'YES' if (eval(eq) == int(r)) else 'NO'
    print(f'Case {i+1}: {ans}')
