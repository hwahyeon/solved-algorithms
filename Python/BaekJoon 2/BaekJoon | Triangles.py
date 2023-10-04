def triangles(n, l):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c = alpha.index(l)
    
    for i in range(1, n + 1):
        print(alpha[c] * i)
        c = (c + 1) % 26
        
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, l = input().split()
        triangles(int(n), l)
        print()
