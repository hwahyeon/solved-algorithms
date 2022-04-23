def direction(facing, turn):
    turn %= 360
    det = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    return det[(det.index(facing) + (turn//45)) % len(det)]
