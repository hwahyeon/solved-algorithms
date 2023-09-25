flip = {
    "1": {"d": "q", "b": "p", "q": "d", "p": "b"},
    "2": {"d": "b", "b": "d", "q": "p", "p": "q"}
}

n, mode = input().split()
for _ in range(int(n)):
    s = input()
    result = ''.join(flip[mode].get(char, char) for char in s)
    print(result)
