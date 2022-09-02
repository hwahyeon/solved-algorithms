class List:
    def remove_(self, integer_list, values_list):
        r = []
        s = set(values_list)
        for i in integer_list:
            if i not in s:
                r.append(i)
        return r
