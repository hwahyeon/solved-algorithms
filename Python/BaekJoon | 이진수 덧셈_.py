for _ in range(int(input())):
    a1, b1 = input().split()
    a2, b2 = int(f'0b{a1}', 2), int(f'0b{b1}', 2)
    print(bin(a2+b2)[2:])
