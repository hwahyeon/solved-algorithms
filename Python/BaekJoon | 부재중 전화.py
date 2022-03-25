N, L, D = map(int, input().split())

song = ([0]*L + [1]*5)*N

bell = 0
while bell < len(song):
    if song[bell] == 1:
        break
    bell += D
print(bell)
