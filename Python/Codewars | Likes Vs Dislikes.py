def like_or_dislike(lst):
    like, dislike = 0, 0
    for i in lst:
        if i == 'Like' and like == 0:
            like += 1
            dislike = 0
        elif i == 'Like' and like > 0:
            like -= 1
            dislike = 0
        elif i == 'Dislike' and dislike == 0:
            dislike += 1
            like = 0
        elif i == 'Dislike' and dislike > 0:
            dislike -= 1
            like = 0
    if like == dislike == 0:
        return 'Nothing'
    elif like > dislike:
        return 'Like'
    else:
        return 'Dislike'
