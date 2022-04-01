def palindrome(num,s):
    res = []
    if (type(num) != int) or num < 0:
        return 'Not valid'
    elif (type(s) != int) or s < 0:
        return 'Not valid'
    else:
        cnt = s
        while cnt != 0:
            string = str(num)
            if string == string[::-1] and num > 10:
                res.append(num)
                cnt -= 1
            num += 1
    return res
