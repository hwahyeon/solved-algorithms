for _ in range(int(input())):
    S, N = input().split('-')
    A = 0
    for i in range(3):
        A += (ord(S[i]) - 65) * 26 ** (2-i)
    print('nice') if abs(int(N) - A) <= 100 else print('not nice')
