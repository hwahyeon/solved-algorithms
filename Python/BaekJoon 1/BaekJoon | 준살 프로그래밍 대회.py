n = int(input())
for i in range(n):
    print("Scenario #{}:".format(i + 1))
    l_num = int(input())
    lst1 = []
    for j in range(l_num):
        lst1.append(input())
    p_num = int(input())
    for k in range(p_num):
        lst2 = list(map(int, input().split()))
        for l in lst2[1:]:
            print(lst1[l],end="")
        print()
    if i != n - 1:
        print()
