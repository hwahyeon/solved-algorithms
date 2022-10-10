import re

def hex_hash(code):
    c = 0
    for i in re.sub(r'[^0-9]', '', code.encode('utf-8').hex()):
        c += int(i)
    return c
