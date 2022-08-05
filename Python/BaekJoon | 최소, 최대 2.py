for _ in range(int(input())):
    n = input()
    l = list(list(map(int, input().split())))
    print(f'{min(l)} {max(l)}')
