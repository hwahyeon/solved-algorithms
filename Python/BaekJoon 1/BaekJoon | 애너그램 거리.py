for n in range(int(input())):
    a = input()
    b = input()
    r = [0] * 26
    for i in a:
        r[ord(i)-97] += 1
    for j in b:
        r[ord(j)-97] -= 1
    print(f'Case #{n+1}: {sum(map(abs, r))}')
