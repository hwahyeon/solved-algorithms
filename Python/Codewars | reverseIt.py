def reverse_it(data):
    if type(data) not in (str, int, float):
        return data
    return type(data)(str(data)[::-1])
