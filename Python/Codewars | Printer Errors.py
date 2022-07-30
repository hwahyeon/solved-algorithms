def printer_error(s):
    res = 0
    for i in s:
        if i not in 'abcdefghijklm':
           res += 1 
    return f'{res}/{len(s)}'
