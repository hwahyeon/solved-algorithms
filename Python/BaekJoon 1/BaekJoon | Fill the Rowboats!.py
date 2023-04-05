n = int(input())
r = ''
for i in range(1, n + 1):
    if i % 6 == 0:
        r += str(i) + ' Go! '
    else:
        r += str(i) + ' '
if n % 6 != 0:
    r += 'Go!'
print(r)
