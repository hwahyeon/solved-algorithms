socks = []
for _ in range(5):
    s = input()
    if s in socks:
        socks.remove(s)
    else:
        socks.append(s)
print(*socks)
