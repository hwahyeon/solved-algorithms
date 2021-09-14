import string
lower = string.ascii_lowercase
word = input()
for x in lower:
    print(word.find(x))
