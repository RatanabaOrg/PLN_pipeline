def replace_abbreviations_in_text(words):
    
    abbreviations = {
        'im': ['i', 'am'],
        'asap': ['as', 'soon', 'as', 'possible'],
        'ill': ['i', 'will'],
        'pm': ['post', 'meridiem'],
        'am': ['ante', 'meridiem'],
        'fyi': ['for', 'your', 'information'],
        'btw': ['by', 'the', 'way'],
        'lol': ['laughing', 'out', 'loud'],
        'idk': ["I", "don't", "know"],
        'brb': ['be', 'right', 'back'],
        'bbl': ['be', 'back', 'later'],
        'omw': ['on', 'my', 'way'],
        'wbu': ['what', 'about', 'you'],
        'tbh': ['to', 'be', 'honest'],
        'np': ['no', 'problem'],
        'gtg': ['got', 'to', 'go'],
        'gr8': ['great'],
        'lmk': ['let', 'me', 'know'],
        'nvm': ['never', 'mind'],
        'thx': ['thanks'],
        'pls': ['please'],
        'u': ['you'],
        'r': ['are'],
        'msg': ['message'],
        'txt': ['text'],
        'cu': ['see', 'you'],
        'smh': ['shaking', 'my', 'head'],
        'imo': ['in', 'my', 'opinion'],
        'ikr': ['I', 'know', 'right?'],
        'b4': ['before'],
        'rn': ['right', 'now'],
        'bc': ['because'],
        'xoxo': ['hugs', 'and', 'kisses'],
        'afaik': ['as', 'far', 'as', 'I', 'know'],
        'aka': ['also', 'known', 'as'],
        'tba': ['to', 'be', 'announced'],
        'tbd': ['to', 'be', 'determined'],
        'rofl': ['rolling', 'on', 'the', 'floor', 'laughing'],
        'wtf': ['what', 'the', 'heck'],
        'bff': ['best', 'friends', 'forever']
    }

    new_words = []  # Use a list to accumulate the new words

    for word in words:
        if word in abbreviations:
            new_words.extend(abbreviations[word])  # Extend the new_words list with the expansion
        else:
            new_words.append(word)  # Keep the original word if it's not an abbreviation

    return new_words