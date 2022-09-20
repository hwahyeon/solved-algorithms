def find_missing_letter(chars):
    m = ord(min(chars))
    for i in chars:
        if m == ord(i):
            m += 1
        else:
            return chr(m)
