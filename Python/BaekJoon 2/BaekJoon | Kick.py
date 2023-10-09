s = input()
r = 0
for i in range(len(s)):
    if s[i:i+4] == 'kick':
        r += 1
print(r)
