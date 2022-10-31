import math

def strong_num(number):
    s = str(number)
    for i in s:
        number -= math.factorial(int(i))
    return "STRONG!!!!" if number == 0 else "Not Strong !!"
