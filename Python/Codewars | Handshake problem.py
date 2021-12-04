import math

def get_participants(handshakes):
    return math.ceil((1+(1+8*handshakes)**0.5)/2)
