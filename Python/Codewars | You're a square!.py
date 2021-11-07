def is_square(n):    
    try:
        if n**0.5 == int(n**0.5):
            return True
        else:
            return False
    except:
        return False
