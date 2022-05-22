def kill_monsters(health, monsters, damage):
    if monsters % 3 == 0:
        hits = (monsters//3) - 1
        damage = hits * damage
        health -= damage
    else:
        hits = (monsters//3)
        damage = hits * damage
        health -= damage
    if health > 0:
        return f'hits: {hits}, damage: {damage}, health: {health}'
    else:
        return 'hero died'
