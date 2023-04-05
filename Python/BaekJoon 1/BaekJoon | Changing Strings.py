s = input()
num_u = s.index('U')
num_f= s[::-1].index('F')
print(f"{'-'*num_u}{'U'}{'C'*(len(s)-num_u-num_f-2)}{'F'}{'-'*num_f}")
