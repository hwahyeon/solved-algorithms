def is_opposite(s1,s2):
    if len(s1) == 0:
        return False
    for i in range(len(s1)):
        if s1[i].islower() == s2[i].islower():
            return False
    return True
