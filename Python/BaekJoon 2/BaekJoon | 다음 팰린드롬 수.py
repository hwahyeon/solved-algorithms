def next_palindrome(s):
    l = len(s)
    
    def create_right(s):
        l = len(s)
        if l % 2 == 0:
            return s[:l//2] + s[:l//2][::-1]
        else:
            return s[:l//2] + s[l//2] + s[:l//2][::-1]

    def increment_from_middle(s):
        chars = list(s)
        i = len(chars) // 2
        if len(chars) % 2 == 0:
            i -= 1
        while chars[i] == '9' and i >= 0:
            chars[i] = '0'
            if i != len(chars) - i - 1:
                chars[len(chars) - i - 1] = '0'
            i -= 1
        if i >= 0:
            chars[i] = str(int(chars[i]) + 1)
            chars[len(chars) - i - 1] = chars[i]
        else:
            chars[0] = '1'
            chars.append('1')
        return ''.join(chars)

    r = create_right(s)
    if int(r) >= int(s):
        return r

    r = increment_from_middle(s)
    return create_right(r)

n = input()
print(next_palindrome(str(int(n) + 1)))
