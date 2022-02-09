def leo(oscar):
    if oscar > 88:
        oscar = 89
    elif oscar < 86: 
        oscar = 87

    return ["Not even for Wolf of wallstreet?!",
     "When will you give Leo an Oscar?",
     "Leo finally won the oscar! Leo is happy",
     "Leo got one already!"][oscar-86]
