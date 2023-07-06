for _ in range(int(input())):
    print(input().translate(str.maketrans('yaeiouYAEIOU', 'aeiouyAEIOUY')))
