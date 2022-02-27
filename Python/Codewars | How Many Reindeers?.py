def reindeer(presents):
    if presents > 180:
        raise Exception('Threw an error!')
    
    a, b = divmod(presents, 30)
    if b != 0:
        return a + 3
    else:
        return a + 2
