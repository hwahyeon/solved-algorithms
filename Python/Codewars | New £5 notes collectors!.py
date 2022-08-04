def get_new_notes(salary,bills):
    res = (salary - sum(bills))//5
    return res if res > 0 else 0
