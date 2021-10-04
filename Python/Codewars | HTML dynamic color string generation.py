import random
def generate_color_rgb():
    total = '0123456789abcdef'
    res = '#'
    for i in range(6):
        res += random.choice(total)
    return res
