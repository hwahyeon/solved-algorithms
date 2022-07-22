def calculator(txt):
    a, b, c = txt.split(' ')
    return '.' * eval(f"{a.count('.')}{b}{c.count('.')}")
