def format_money(amount):
    res = str(amount).split('.')
    res.append('0')
    return f'${res[0]}.{res[1]:0<2}'
