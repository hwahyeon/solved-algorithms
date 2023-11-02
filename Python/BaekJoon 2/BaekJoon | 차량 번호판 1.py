s = input()

ans = 26 if s[0] == 'c' else 10

for i in range(1, len(s)):
    if s[i] == 'c':
        ans *= 25 if s[i - 1] == 'c' else 26
    else:
        ans *= 9 if s[i - 1] == 'd' else 10

print(ans)
