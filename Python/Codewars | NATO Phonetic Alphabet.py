def nato(word):
    phonetic = ['Alpha',
            'Bravo',
            'Charlie',
            'Delta',
            'Echo',
            'Foxtrot',
            'Golf',
            'Hotel',
            'India',
            'Juliett',
            'Kilo',
            'Lima',
            'Mike',
            'November',
            'Oscar',
            'Papa',
            'Quebec',
            'Romeo',
            'Sierra',
            'Tango',
            'Uniform',
            'Victor',
            'Whiskey',
            'X-ray',
            'Yankee',
            'Zulu']
    r = []
    for i in word.lower():
        r.append(phonetic[ord(i)-97])
    return ' '.join(r)
