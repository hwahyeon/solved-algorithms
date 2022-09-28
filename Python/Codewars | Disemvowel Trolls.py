import re
def disemvowel(string_):
    return re.sub(r"[AEOUIaeoui]", "", string_)
