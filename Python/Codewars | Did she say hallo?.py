def validate_hello(greetings):
    greet = ['hello',
        'ciao',
        'salut',
        'hallo',
        'hola',
        'ahoj',
        'czesc']
    for i in greet:
        if i in greetings.lower():
            return True
    return False
