import math

w, l = map(int, input().split())
acr = w * l / 4840

print(math.ceil(acr / 5))
