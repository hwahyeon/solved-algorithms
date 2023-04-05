n = int(input())
s = input()
print(min(n, s.count("S")+s.count("L")//2+1))
