def star_sign(date): 
    mon, day = str(date.month), str(date.day)
    if len(day) < 2:
        day = '0'+day
    birth = int(mon+day)
    if 121 <= birth <= 219:
        return 'Aquarius'
    elif 220 <= birth <= 320:
        return 'Pisces'
    elif 321 <= birth <= 420:
        return 'Aries'
    elif 421 <= birth <= 521:
        return 'Taurus'
    elif 522 <= birth <= 621:
        return 'Gemini'
    elif 622 <= birth <= 722:
        return 'Cancer'
    elif 723 <= birth <= 823:
        return 'Leo'
    elif 824 <= birth <= 923:
        return 'Virgo'
    elif 924 <= birth <= 1023:
        return 'Libra'
    elif 1024 <= birth <= 1122:
        return 'Scorpio'
    elif 1123 <= birth <= 1221:
        return 'Sagittarius'
    else:
        return 'Capricorn'
