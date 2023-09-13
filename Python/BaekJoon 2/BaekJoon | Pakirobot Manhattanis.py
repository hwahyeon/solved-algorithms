N = int(input())
steps = input()

N_steps = steps.count('N')
S_steps = steps.count('S')
E_steps = steps.count('E')
W_steps = steps.count('W')

print(abs(N_steps - S_steps) + abs(E_steps - W_steps))
