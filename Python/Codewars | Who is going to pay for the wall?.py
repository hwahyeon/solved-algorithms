def who_is_paying(name):
    return [name, name[:2]] if len(name) > 2 else [name]
