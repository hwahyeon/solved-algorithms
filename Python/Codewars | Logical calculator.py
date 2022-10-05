def logical_calc(array, op):
    bool = array[0]
    if op == 'AND':
        oper = 'and'
    elif op == 'OR':
        oper = 'or'
    elif op == 'XOR':
        oper = '!='
    for i in range(1, len(array)):
        bool = eval(f"{bool} {oper} {array[i]}")
    return bool
