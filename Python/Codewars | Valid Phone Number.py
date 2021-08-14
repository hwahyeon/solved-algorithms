import re

def valid_phone_number(phone_number):
    regex = re.compile(r'^\(\d{3}\)\s\d{3}\-\d{4}$')
    return bool(regex.match(phone_number))
