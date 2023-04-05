for i in range(int(input())):
    n = int(input())
    s = input()
    n += s.count('c') - s.count('b')
    print(f'Data Set {i+1}:')
    print(n)
    print()
