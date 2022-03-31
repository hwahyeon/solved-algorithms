def palindrome(num):
    if (type(num) != int) or num < 0:
        return 'Not valid'
    else:
        string = str(num)
        n = len(string)
        if n % 2 == 0:
            res1, res2 = int(n/2), int(n/2)
        else:
            res1, res2 = int(n/2-0.5), int(n/2+0.5)
        return string[:res1] == string[res2:][::-1]
 


#######
def palindrome(num):
    if type(num) is not int or num < 0:
        return "Not valid"
    return num == int(str(num)[::-1])
