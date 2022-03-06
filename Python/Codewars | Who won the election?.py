def get_winner(ballots):
    member = sorted(list(set(ballots)))
    max = 0
    max_member = None
    for n, i in enumerate(member):
        cnt = ballots.count(i)
        if max < cnt and cnt > (len(ballots)/2):
            max = cnt
            max_member = n

    return (member[max_member]) if max_member != None else None
