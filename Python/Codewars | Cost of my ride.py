def insurance(age, size, num_of_days): 
    cost = 0
    cost += num_of_days * 50 
    if age < 25:
        cost += 10 * num_of_days
    add_cost = 0 if size == 'economy' else (10 if size == 'medium' else 15)
    cost += add_cost * num_of_days
    cost = 0 if num_of_days < 0 else cost
    return cost
