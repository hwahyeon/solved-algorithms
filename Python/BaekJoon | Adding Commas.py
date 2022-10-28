import re
p = "(\d)(?=(\d{3})+(?!\d))"
r = r"\1,"
print(re.sub(p, r, input()))
