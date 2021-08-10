def vowel_back(s):
    s = list(s)
    for i in range(len(s)):
        if s[i]=='t' or s[i]=='f' or s[i]=='i' or s[i]=='v':
            s[i]= s[i]
        elif s[i]=='c' or s[i]=='o':
            s[i] = chr((ord(s[i]) - ord('a') - 1) % 26 + ord('a'))
        elif s[i] == 'd':
            s[i] = chr((ord(s[i]) - ord('a') - 3) % 26 + ord('a'))
        elif s[i] == 'e':
            s[i] = chr((ord(s[i]) - ord('a') - 4) % 26 + ord('a'))
        elif s[i] == 'a' or s[i] == 'u':
            s[i] = chr((ord(s[i]) - ord('a') - 5) % 26 + ord('a'))
        else:
            s[i] = chr((ord(s[i]) - ord('a') + 9) % 26 + ord('a'))

    return "".join(s)
