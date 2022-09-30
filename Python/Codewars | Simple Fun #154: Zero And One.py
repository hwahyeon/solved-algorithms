def zero_and_one(s):
    for i in range(len(s)-1):
        if s[i:i+2] == '01' or s[i:i+2] == '10':
            s = s[:i] + '  ' + s[i+2:]
    return len(s) - s.count(' ')
