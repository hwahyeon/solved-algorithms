def to_chinese_numeral(n):
    n_ = abs(n)
    int_ = int(n_)
    str_ = str(int_)
    str_all = str(n_)
    lst_ = list(map(int, list(str(int_))))
    rev_ = list(reversed(lst_))
    times = '一十百千万'
    han = '零一二三四五六七八九十'

    def Int_chi(rev_, n):
        for a, i in enumerate(rev_):
            rev_[a] = han[i]+times[a]
        res_ = list(reversed(rev_))
        res_[-1] = han[int(str_[-1])]
        if res_[-1] == '零':
            del res_[-1]
        if 20 > abs(n) > 9:
            Int_Chi1 = "".join(res_).replace('零十', '0').replace('一十', '十')
        else:
            Int_Chi1 = "".join(res_).replace('零十', '0').replace('零百', '0').replace('零千', '0')
        Int_Chi2 = Int_Chi1.replace('0', '零').replace('零零零', '零').replace('零零', '零')
        if Int_Chi2 == '':
            Int_Chi = '零'
        elif Int_Chi2[-1] == '零' and len(Int_Chi2) > 1:
            Int_Chi = Int_Chi2[:-1]
        else:
            Int_Chi = Int_Chi2
        return Int_Chi

    def Dec_chi(no):
        all_lst = list(str(no))
        all_lst.index('.')
        res_lst = []
        for i in all_lst[all_lst.index('.'):]:
            if i == '.':
                res_lst.append('点')
            else:
                res_lst.append(han[int(i)])
        return "".join(res_lst)
    
    if n==0:
        return '零'
    elif ('.' in str_all) and n > 0:
        return (Int_chi(rev_, n)+Dec_chi(n))
    elif ('.' in str_all) and n < 0:
        return ('负'+Int_chi(rev_, n)+Dec_chi(n))
    elif n > 0:
        return (Int_chi(rev_, n))
    else:
        return ('负'+Int_chi(rev_, n))
