def encryptor(key, message):
    alpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key %= 26
    res = ''
    
    for i in message:
        if i in alpha:
            res += alpha[alpha.index(i)+key]
        else:
            res += i
    return res
