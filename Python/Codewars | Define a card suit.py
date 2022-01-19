def define_suit(card):
    if card[-1].lower() == 'c':
        return 'clubs'
    elif card[-1].lower() == 'd':
        return 'diamonds'
    elif card[-1].lower() == 'h':
        return 'hearts'
    else:
        return 'spades'
