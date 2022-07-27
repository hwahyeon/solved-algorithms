def remove_rotten(bag_of_fruits):
    if bag_of_fruits == None:
        return []
    res = []
    for i in bag_of_fruits:
        res.append(i.replace('rotten', '').lower())
    return res
