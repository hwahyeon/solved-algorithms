n = int(input())
s = n
cnt = 0

while 1:
    s = (s%10 * 10) + ((s//10 + s%10) % 10)
    cnt += 1
    if s == n:
        break

print(cnt)
