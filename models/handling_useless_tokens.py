import re

def handling_useless_tokens(words):
    cleaned_words = []
    for word in words:
        cleaned_word = re.sub(r'[^\w\s]', '', word).lower()
        if cleaned_word:
            cleaned_words.append(cleaned_word)
    return cleaned_words
