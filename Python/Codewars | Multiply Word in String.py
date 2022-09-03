def modify_multiply(st, loc, num):
    l = list(st.split())
    return ((l[loc] + '-')* num)[:-1]
