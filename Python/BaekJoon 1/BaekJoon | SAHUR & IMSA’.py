for i in range(1, int(input())+1):
    h, m = map(int, input().split())
    if m >= 45:
        print(f'Case #{i}: {h} {m-45}')
    elif h == 0:
        print(f'Case #{i}: {h-1+24} {m-45+60}')
    else:
        print(f'Case #{i}: {h-1} {m-45+60}')
