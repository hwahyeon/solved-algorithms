def greatest_common_factor(seq):
    def GCD(x, y):
        while y>0:
          x,y=y,x%y
        return x
    gcd = seq[0]
    for i in seq:
        gcd = GCD(gcd, i)
    return gcd
