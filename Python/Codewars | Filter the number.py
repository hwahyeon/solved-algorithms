import re

def filter_string(string):
    return int(re.sub(r'[^0-9]', '', string))
