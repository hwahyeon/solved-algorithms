import re
def is_it_a_num(s: str) -> str:
    num = re.sub(r'[^0-9]', '', s)
    if len(num) != 11:
        return 'Not a phone number'
    elif num[0] != '0':
        return 'Not a phone number'
    else:
        return num
