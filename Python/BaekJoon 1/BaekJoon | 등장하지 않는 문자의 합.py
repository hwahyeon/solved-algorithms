for _ in range(int(input())):
    cnt = [0] * 26
    s = ''.join(set(input()))
    for i in s:
        cnt[ord(i) - 65] += ord(i)
    print(2015 - sum(cnt))
