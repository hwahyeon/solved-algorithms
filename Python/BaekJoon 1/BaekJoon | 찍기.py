n = int(input())
o = input()
s1 = ('ABC'*n)[:n]
s2 = ('BABC'*n)[:n]
s3 = ('CCAABB'*n)[:n]

def cnt(str1, str2, n):
    c = 0
    for i in range(n):
        if str1[i] == str2[i]:
            c += 1
    return c

A, B, G = cnt(o, s1, n), cnt(o, s2, n), cnt(o, s3, n)
m = max(A, B, G)
print(m)
if m == A:
    print("Adrian")
if m == B:
    print("Bruno")
if m == G:
    print("Goran")
