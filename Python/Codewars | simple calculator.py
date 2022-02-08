def calculator(x,y,op):
    return eval(str(x)+op+str(y)) if op in ['+','-','*','/'] and type(x) == int and type(y) == int else "unknown value"
