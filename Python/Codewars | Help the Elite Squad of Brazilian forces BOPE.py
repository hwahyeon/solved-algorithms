from math import ceil

def mag_number(tuple):
    if tuple[0] == 'PT92':
        n = 17
    elif tuple[0] == 'M4A1' or tuple[0] == 'M16A2':
        n = 30
    elif tuple[0] == 'PSG1':
        n = 5
    return ceil(tuple[1]*3/n)
