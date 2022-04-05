alpha = ['a', 'e', 'i', 'o', 'u']
beta = ['apa', 'epe', 'ipi', 'opo', 'upu']

string = input()
for i in range(5):
    string = string.replace(beta[i], alpha[i])
print(string)
