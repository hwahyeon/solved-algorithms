def cannons_ready(gunners):
    for k, v in gunners.items():
        if v == 'nay':
            return 'Shiver me timbers!'
    return 'Fire!'
