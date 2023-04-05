while 1:
    a, b = input().split()
    if a == b == '0':
        break
    zstring = max(len(a), len(b))
    a = a.zfill(zstring)
    b = b.zfill(zstring)
    cnt= 0
    carry = 0
    for i in range(zstring-1, -1, -1):
        res = int(a[i]) + int(b[i]) + carry
        carry = 0
        if res >= 10:
            cnt += 1
            carry = 1
    print(cnt)
