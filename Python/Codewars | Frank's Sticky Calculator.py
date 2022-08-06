def sticky_calc(operation, val1, val2):
    val1, val2 = round(val1), round(val2)
    return round(eval((str(val1) + str(val2)) + operation + str(val2)))
