import sys

s = sys.stdin.read().replace(' ', '').replace('\n', '')
alphabet = [0]*26
for line in s:
    alphabet[ord(line)-97] += 1
m = max(alphabet)
for i in range(26):
    if alphabet[i] == m:
        print(chr(97+i), end='')
