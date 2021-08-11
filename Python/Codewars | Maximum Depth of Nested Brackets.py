def strings_in_max_depth(S):
    def str_to_lst(Str):
        lst = list(Str)
        SUM = 0
        for i, l in zip(lst, range(len(lst))):
            if i == '(':
                SUM += 1
                lst[l] = SUM
            elif i == ')':
                lst[l] = SUM
                SUM -= 1
            else:
                pass
        return lst

    def MAX_value(lst):
        max_lst = []
        for i in lst:
            if str(type(i)) == "<class 'int'>":
                max_lst.append(i)
        return max(max_lst)

    def Locate(lst, max_num):
        loc = []
        num = 0
        for i in lst:
            num += 1
            if i == max_num:
                loc.append(num)
            else:
                pass
        return loc

    def res_let(locate,S):
        noo = 0
        res_lst = []
        for i in range(int(len(locate)/2)):
            res_lst.append(S[locate[noo]:locate[noo + 1] - 1])
            noo += 2
        return res_lst


    res_lst2 = []
    if S.find('(') != -1:
        return res_let(Locate(str_to_lst(S), MAX_value(str_to_lst(S))),S)
    else:
        res_lst2.append(S)
        return res_lst2
