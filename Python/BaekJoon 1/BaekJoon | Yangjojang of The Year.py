len_tot = int(input())
for i_tot in range(len_tot):
    len_ = int(input())
    res = {}
    for i in range(len_):
        name, no_ = input().split(' ')
        res[name] = int(no_)
    print([k for k,v in res.items() if max(res.values()) == v][0])
