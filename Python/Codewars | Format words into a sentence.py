def format_words(words):
    if str(type(words)) != "<class 'list'>":
        return ""
    else:
        words = ' '.join(words).split()
        if len(words) == 0:
            return ""
        elif len(words) == 1:
            return str(words[0])
        else:
            for n, i in enumerate(words[:-1]):
                words[n] = i+', '
            words[-1] = 'and ' + words[-1]
            return ''.join(words).replace(', and', ' and')
